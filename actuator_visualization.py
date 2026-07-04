import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 1. Данные и расчеты
d31, d33 = -274e-12, 593e-12
L, W, H = 0.02, 0.005, 0.005
U = 500
E3 = U / L

# Относительные деформации
S1 = d31 * E3
S2 = d31 * E3
S3 = d33 * E3

# Абсолютные перемещения
dw, dh, dl = S1 * W, S2 * H, S3 * L

# Коэффициент масштабирования для визуализации (чтобы увидеть микрометры)
scale = 1e5 

def get_cube_verts(w, h, l):
    """Генерирует координаты 8 вершин параллелепипеда"""
    return np.array([
        [0, 0, 0], [w, 0, 0], [w, h, 0], [0, h, 0],
        [0, 0, l], [w, 0, l], [w, h, l], [0, h, l]
    ])

verts_orig = get_cube_verts(W, H, L)
verts_def  = get_cube_verts(W + dw*scale, H + dh*scale, L + dl*scale)

# 2. Визуализация
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

def plot_cube(ax, verts, color, label, alpha=0.2):
    faces = [[verts[0], verts[1], verts[5], verts[4]],
             [verts[2], verts[3], verts[7], verts[6]],
             [verts[0], verts[1], verts[2], verts[3]],
             [verts[4], verts[5], verts[6], verts[7]],
             [verts[0], verts[4], verts[7], verts[3]],
             [verts[1], verts[5], verts[6], verts[2]]]
    poly = Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors=color, alpha=alpha)
    ax.add_collection3d(poly)

plot_cube(ax, verts_orig, 'gray', 'Оригинал', 0.1)
plot_cube(ax, verts_def, 'blue', 'Деформирован (x10^5)')

ax.set_title(f'Деформация актуатора PZT-5H при {U}В\n(Тензорный расчет)')
ax.set_xlabel('X (м)'); ax.set_ylabel('Y (м)'); ax.set_zlabel('Z (м)')
ax.set_zlim(0, 0.025)
plt.show()

print(f"Реальное удлинение (dL): {dl*1e6:.3f} мкм")
print(f"Реальное сужение (dW): {dw*1e6:.3f} мкм")
