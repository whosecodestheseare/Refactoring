import numpy as np
import matplotlib.pyplot as plt
import imageio_ffmpeg
from matplotlib.animation import FFMpegWriter, FuncAnimation


FPS = 30
DURATION_SECONDS = 10
FRAME_COUNT = FPS * DURATION_SECONDS
OUTPUT_FILE = "sine_wave_3d.mp4"

plt.rcParams["animation.ffmpeg_path"] = imageio_ffmpeg.get_ffmpeg_exe()

x = np.linspace(0, 4 * np.pi, 400)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")
line, = ax.plot(x, np.zeros_like(x), np.zeros_like(x), color="royalblue", linewidth=2.5)

ax.set_title("Moving 3D Sine Wave")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(-1.2, 1.2)
ax.view_init(elev=25, azim=-65)


def update(frame):
    phase = 2 * np.pi * frame / FRAME_COUNT
    y = np.sin(x - 2 * phase)
    z = 0.55 * np.cos(x - 2 * phase)
    line.set_data(x, y)
    line.set_3d_properties(z)
    return (line,)


animation = FuncAnimation(
    fig,
    update,
    frames=FRAME_COUNT,
    interval=1000 / FPS,
    blit=False,
)

writer = FFMpegWriter(fps=FPS, metadata={"title": "Moving 3D Sine Wave"})
animation.save(OUTPUT_FILE, writer=writer)
plt.show()