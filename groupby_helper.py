class GroupbyHelper:
    def __init__(self):
        # sturcture of new features for analysis by groups

        self.derived_features = {
            'ratings': [
                ('num_listings', lambda x: int(len(x))), 
                ('avg_ratings', lambda x: round(x.mean(), 2)),
                ('5_star_rating(%)', lambda x: round(x[x == 5].count()*100 / len(x), 2))
            ],
            'number_of_reviews': [
                ('total_reviews', lambda x: x.sum())
            ]
        }

    def get_grouped_df(self, df, groupby_cols):
        # custom function to group data by different columns along with added features

        grouped_df = df.groupby(groupby_cols, sort=False).agg(self.derived_features).reset_index()
        grouped_df.columns = [col[1] if col[1] != '' else col[0] for col in grouped_df.columns]
        grouped_df['review_density'] = round(grouped_df['total_reviews'] / grouped_df['num_listings'], 2)

        return grouped_df
    
    
    def sort_group_df(self, grouped_df, col, asc=False):
        # function to sort grouped df

        return grouped_df.sort_values(by=col, ascending=asc).reset_index(drop=True)


    def get_filtered_df(self, group_df, listings_threshold=None, ratings_threshold=None, total_reviews_threshold=None):
        # creating a function to create one filter for each grouped_df formed by some unique filters for analysis

        avg_of_avg_ratings = ratings_threshold or group_df['avg_ratings'].mean()
        avg_num_listings = listings_threshold or group_df['num_listings'].mean()
        avg_total_reviews = total_reviews_threshold or group_df['total_reviews'].mean()

        # show the filter thresholds
        print(f"avg_of_avg_ratings: {avg_of_avg_ratings}, avg_num_listings: {avg_num_listings}, avg_total_reviews: {avg_total_reviews}")

        num_listings_filter = group_df['num_listings'] > avg_num_listings
        avg_ratings_filter = group_df['avg_ratings'] > avg_of_avg_ratings
        total_reviews_filter = group_df['total_reviews'] > avg_total_reviews

        combined_filter = num_listings_filter & avg_ratings_filter & total_reviews_filter

        return group_df[combined_filter]

    def get_group_intersection_df(self, group_df1, group_df2, group_df3, merge_cols):
        # return the rows that are present in each group df

        first_intersection_df = group_df1.merge(group_df2, on=merge_cols+['num_listings'], how='inner')
        final_intersection_df = first_intersection_df.merge(group_df3, on=merge_cols+['num_listings'], how='inner')

        # final_intersection_df.drop('num_listings_y', axis=1, inplace=True)
        # final_intersection_df.rename(columns={'num_listings_x': 'num_listings'}, inplace=True)

        return final_intersection_df