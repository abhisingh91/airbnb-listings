from scipy.stats import shapiro, levene

class HypothesisHelper:
    def __init__(self):
        pass

    # create a function to get to a conclusion of accepting or rejecting null hypothesis based on p-value

    def get_p_value_based_conclusion(self, p_value, alpha=0.05):
        print(f"p-value: {p_value:.4f}")
        if p_value <= alpha:
            print(f"Reject the null hypothesis")  # Reject the null hypothesis
        else:
            print('Falied to reject the null hypothesis')  # Fail to reject the null hypothesis

    def has_normal_dist(self, data):
        test_stat_normality, p_value_normality = shapiro(data)
        print(f"p-value: {p_value_normality:.4f}")

        if p_value_normality < 0.05:
            return 0
        return 1
    
    def check_variance_homogeneity(self, groups):
        test_stat_var, p_value_var= levene(*groups)

        print(f"p-value: {p_value_var:.4f}")
        if p_value_var <0.05:
            print("Reject null hypothesis >> The variances of the samples are different.")
        else:
            print("Fail to reject null hypothesis >> The variances of the samples are same.")
        