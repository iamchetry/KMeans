from numpy import *
from matplotlib import pyplot as plt


def define_data(num_of_vars=None, length=None):
    return random.rand(length, num_of_vars)


def initialize_centroids(num_clusters=None, data_=None):
    return random.uniform(data_.min(), data_.max(), size=(num_clusters, size(data_, 1)))


def euclidean_dist(data_vec=None, cluster_means=None):
    return linalg.norm(data_vec-cluster_means, axis=1)


def allocate_clusters(data_=None, cluster_means=None, cluster=None):
    for k in range(len(data_)):
        cluster[k] = argmin(euclidean_dist(data_vec=data_[k, :], cluster_means=cluster_means))
    return cluster


def update_centroids(data_=None, num_clusters=None, cluster_means=None, cluster=None):
    clustered_data = c_[data_, cluster]
    for k in range(num_clusters):
        cluster_points = clustered_data[clustered_data[:, -1] == k][:, :-1]
        cluster_means[k] = mean(cluster_points, axis=0)

    return cluster_means


def k_means(data_=None, cluster_means=None, num_clusters=None):
    cluster_new = zeros((size(cluster_means, 0), size(data_, 1)))
    dist_ = euclidean_dist(data_vec=cluster_new, cluster_means=cluster_means)
    cluster = zeros(len(data_))

    while all(dist_ != 0):
        cluster = allocate_clusters(data_=data_, cluster_means=cluster_means, cluster=cluster)
        cluster_means_updated = update_centroids(data_=data_, num_clusters=num_clusters, cluster_means=cluster_means,
                                                 cluster=cluster)
        dist_ = euclidean_dist(data_vec=cluster_means_updated, cluster_means=cluster_means)
        cluster_means = cluster_means_updated

    return c_[data_, cluster]


def kmeans_main(num_of_vars=None, length_of_data=None, num_clusters=None):
    data = define_data(num_of_vars=num_of_vars, length=length_of_data)
    centres = initialize_centroids(num_clusters=num_clusters, data_=data)
    return k_means(data_=data, cluster_means=centres, num_clusters=num_clusters)


def scatter_plot(data_=None, colors_tag=None):
    colors_ = [colors_tag[k] for k in data_[:, -1].astype('int')]
    plt.scatter(data_[:, 0], data_[:, 1], c=colors_, alpha=0.5)
    plt.show(block=True)
    plt.interactive(False)
