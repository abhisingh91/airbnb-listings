import seaborn as sns

class PlotHelper:
    def __init__(self):
        pass


    def add_value_labels(self, ax, decimal_count, spacing=5, type_ax='V'):
         # function to add value labels on top of each bar in a bar plot

        for p in ax.patches:
            if type_ax == 'V':
                value = round(p.get_height(), decimal_count)
                if decimal_count == 0:
                    value = int(value)
                ax.annotate(value, (p.get_x() + p.get_width() / 2, p.get_height()),
                            ha='center', va='center', xytext=(0, spacing), textcoords='offset points')
            elif type_ax == 'H':
                value = round(p.get_width(), decimal_count)
                if decimal_count == 0:
                    value = int(value)
                ax.annotate(value, (p.get_width(), p.get_y() + p.get_height() / 2),
                        ha='left', va='center', xytext=(spacing, 0), textcoords='offset points')
    

    def plot_bar_graph(self, x, y, decimal_count, x_size, y_size, data, orient=None, type_ax='V', palette=None, alpha=1):
        # function to do the reduce redundant lines for plotting graphs

        sns.set(rc={'figure.figsize':(x_size, y_size)})   # set the figure size of the plot

        bar_plot_ax = sns.barplot(x=x, y=y, data=data[:10], orient=orient, palette=palette, alpha=alpha)
        self.add_value_labels(bar_plot_ax, decimal_count, type_ax=type_ax)