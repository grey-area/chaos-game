import numpy as np
import matplotlib.pyplot as plt
import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--num-vertices',
        type=int, default=3
    )
    parser.add_argument(
        '--alpha',
        type=float, default=0.5,
        help='Proportion of distance to vertex to hop'
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    angles = np.linspace(0, 2*np.pi, args.num_vertices + 1)[:-1]
    vertices = np.exp(1j * angles)
    vertex_xs = np.imag(vertices)
    vertex_ys = np.real(vertices)

    initial_weights = np.random.random(args.num_vertices)
    initial_weights /= np.sum(initial_weights)
    point = initial_weights.dot(vertices)
    xs = []
    ys = []

    steps = 60000
    for i in range(steps):
        vertex = np.random.choice(vertices)
        point = (1 - args.alpha) * point + args.alpha * vertex
        xs.append(np.imag(point))
        ys.append(np.real(point))

    plt.style.use('dark_background')
    plt.figure(figsize=(7, 7))

    plt.scatter(vertex_xs, vertex_ys, s=20, c='C3', zorder=1)
    plt.scatter(xs[1000:], ys[1000:], s=0.01, c='white', zorder=0)
    plt.axis('off')
    plt.gca().set_aspect('equal')

    x_min = np.min(vertex_xs) * 1.03
    x_max = np.max(vertex_xs) * 1.03
    y_min = np.min(vertex_ys) * 1.03
    y_max = np.max(vertex_ys) * 1.03
    plt.xlim((x_min, x_max))
    plt.ylim((y_min, y_max))
    plt.tight_layout()
    plt.savefig('chaos_game.png', dpi=600)

