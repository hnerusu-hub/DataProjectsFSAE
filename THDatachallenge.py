import polars as pl
import matplotlib.pyplot as plt

df = pl.read_parquet("/Users/hansika/pythonProject/HelloWorld/fs-4-software-intro-projects-main/Data/08102025Endurance1_FirstHalf.parquet")
df = df.filter(pl.col("VDM_GPS_SPEED") > 1)
df = df.filter(pl.col("SME_TEMP_BusCurrent").is_not_null())
df = df.filter(pl.col("SME_TEMP_DC_Bus_V").is_not_null())
rho = 1.225
df = df.with_columns(
    (pl.col("SME_TEMP_DC_Bus_V") * pl.col("SME_TEMP_BusCurrent")).alias("Motor_Power_W")
)

df = df.with_columns((pl.col("VDM_GPS_SPEED") * 0.44704).alias("Speed_mps"))
df = df.with_columns(
    (2 * pl.col("Motor_Power_W") / (rho * pl.col("Speed_mps")**3)).alias("CdA")
)
df = df.filter((pl.col("CdA") > 0) & (pl.col("CdA") < 5))

avg_cda = df["CdA"].mean()
print(f"Estimated CdA: {avg_cda:.3f} m²")
pdf = df.select(["Speed_mps", "CdA"]).to_pandas()

plt.figure(figsize=(8, 5))
plt.scatter(pdf["Speed_mps"], pdf["CdA"], s=8, alpha=0.6, label="Instantaneous CdA")
plt.axhline(avg_cda, color='red', linestyle='--', label=f"Average CdA = {avg_cda:.3f} m²")
plt.xlabel("Speed (m/s)")
plt.ylabel("CdA (m²)")
plt.title("Estimated Drag Coefficient × Cross-sectional Area vs Speed")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()