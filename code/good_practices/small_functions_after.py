def run(path):
    data = read_data(path)
    data = remove_outliers(data)
    fit = fit_model(data)
    plot_fit(data, fit)
    save_results(fit)
