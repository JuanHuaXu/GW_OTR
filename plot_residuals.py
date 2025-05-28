# plot_residuals.py
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse


def load_tensor(path):
    return np.load(path)


def plot_tensor(matrix, title, out_path):
    plt.figure(figsize=(4, 4))
    plt.imshow(matrix, cmap='bwr', interpolation='none')
    plt.colorbar(label='Tensor Value')
    plt.title(title)
    plt.xticks(range(3), ['x', 'y', 'z'])
    plt.yticks(range(3), ['x', 'y', 'z'])
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def main(event_dir):
    pairs = [
        ("Hanford", "Livingston"),
        ("Hanford", "Virgo"),
        ("Livingston", "Virgo")
    ]

    for a, b in pairs:
        delta_file = os.path.join(event_dir, f"{os.path.basename(event_dir)}_delta_{a}_{b}.npy")
        if not os.path.exists(delta_file):
            print(f"Skipping: {delta_file} not found")
            continue

        delta_tensor = load_tensor(delta_file)
        title = f"Residual: {a} – {b}"
        out_file = os.path.join(event_dir, f"{a}_{b}_residual.png")
        plot_tensor(delta_tensor, title, out_file)
        print(f"Saved: {out_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot residual tensors as heatmaps.")
    parser.add_argument("event_dir", type=str, help="Path to event output directory")
    args = parser.parse_args()

    main(args.event_dir)

