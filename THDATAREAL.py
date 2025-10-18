import matplotlib.pyplot as plt
import polars as pl

df = pl.read_parquet("/Users/hansika/pythonProject/HelloWorld/fs-4-software-intro-projects-main/Data/08102025Endurance1_FirstHalf.parquet")


df = df.filter(pl.col("VDM_GPS_Latitude") != 0).filter(pl.col("VDM_GPS_Longitude") != 0)

print(df.columns)

pdf = df.to_pandas()

fig, axs = plt.subplots(2, 2, figsize=(14, 8))
fig.suptitle("Vehicle Telemetry Overview", fontsize=16, fontweight='bold')

# 1️⃣ SPEED vs TORQUE
axs[0, 0].plot(pdf["VDM_GPS_SPEED"], label="GPS Speed (mph)", color='royalblue')
axs[0, 0].plot(pdf["SME_TRQSPD_Torque"], label="Motor Torque (Nm)", color='darkorange', alpha=0.7)
axs[0, 0].set_title("Speed vs Torque")
axs[0, 0].set_xlabel("Time (samples)")
axs[0, 0].set_ylabel("Value")
axs[0, 0].legend()
axs[0, 0].grid(True)


axs[0, 1].plot(pdf["ACC_POWER_PACK_VOLTAGE"], label="Pack Voltage (V)", color='green')
axs[0, 1].plot(pdf["ACC_POWER_CURRENT"], label="Pack Current (A)", color='red', alpha=0.7)
axs[0, 1].plot(pdf["ACC_POWER_SOC"], label="SOC (%)", color='purple', linestyle='--')
axs[0, 1].set_title("Battery Performance")
axs[0, 1].legend()
axs[0, 1].grid(True)


axs[1, 0].plot(pdf["VDM_GPS_Longitude"], pdf["VDM_GPS_Latitude"], color='teal', linewidth=1.5)
axs[1, 0].set_title("GPS Path (Track Map)")
axs[1, 0].set_xlabel("Longitude")
axs[1, 0].set_ylabel("Latitude")
axs[1, 0].grid(True)


axs[1, 1].plot(pdf["TPERIPH_FL_DATA_WHEELSPEED"], label="Front Left", color='dodgerblue')
axs[1, 1].plot(pdf["TPERIPH_BL_DATA_WHEELSPEED"], label="Rear Left", color='darkred')
axs[1, 1].set_title("Wheel Speed Comparison")
axs[1, 1].set_xlabel("Time (samples)")
axs[1, 1].set_ylabel("Speed (mph)")
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()