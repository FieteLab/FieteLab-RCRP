import matplotlib.pyplot as plt
import os


def plot_sample_from_mixture_of_gaussians(assigned_table_seq,
                                          gaussian_samples_seq,
                                          plot_dir):

    plt.scatter(x=gaussian_samples_seq[:, 0],
                y=gaussian_samples_seq[:, 1],
                c=assigned_table_seq)
    plt.savefig(os.path.join(plot_dir, 'sample_from_mixture_of_gaussians.png'))
    plt.show()

