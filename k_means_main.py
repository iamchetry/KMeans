from kmeans_clustering import kmeans_main, scatter_plot


data_ = kmeans_main(num_of_vars=2, length_of_data=100000, num_clusters=4)
scatter_plot(data_=data_, colors_tag=['r', 'g', 'b', 'y'])
