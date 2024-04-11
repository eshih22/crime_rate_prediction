def performCalculations(all_df_reset):
    all_df_reset = calculate_education(all_df_reset)
    all_df_reset = calculateOthers(all_df_reset)
    all_df_reset = calculate_percentage_ages(all_df_reset)
    return all_df_reset


def calculateOthers(all_df_reset):
    all_df_reset['Total'] = all_df_reset['Total Occupied'] + all_df_reset['Renter occupied']
    all_df_reset['Percent Home Occupied'] = all_df_reset['Total Occupied'] / all_df_reset['Total'] * 100
    all_df_reset['Percent Renter Occupied'] = all_df_reset['Renter occupied'] / all_df_reset['Total'] * 100
    all_df_reset['Percent 25+'] = (
            all_df_reset['Percent 25 to 34 years'] +
            all_df_reset['Percent 35 to 44 years'] +
            all_df_reset['Percent 45 to 54 years'] +
            all_df_reset['Percent 55 to 59 years'] +
            all_df_reset['Percent 60 to 64 years'] +
            all_df_reset['Percent 65 to 74 years'] +
            all_df_reset['Percent 75 to 84 years']
    )

    all_df_reset['Percent 14-'] = (
            all_df_reset['Percent Under 5 years'] +
            all_df_reset['Percent 5 to 9 years'] +
            all_df_reset['Percent 10 to 14 years']
    )

    all_df_reset['Percent 15 to 24'] = (
            all_df_reset['Percent 15 to 19 years'] +
            all_df_reset['Percent 20 to 24 years']
    )

    all_df_reset['Percent Uneducated'] = (
            all_df_reset['Percent Population 25 years and over - Less than 9th grade'] +
            all_df_reset['Percent Population 25 years and over - 9th to12th (No Diploma)']
    )

    all_df_reset['Percent Higher Education'] = (
            all_df_reset['Percent Population 25 years and over - Graduate or Prefessional Degree'] +
            all_df_reset["Percent Population 25 years and over - Bachelor's degree"] +
            all_df_reset["Percent Population 25 years and over - Associate's degree"]
    )

    all_df_reset['Sum Uneducated'] = (
            all_df_reset['Population 25 years and over - Less than 9th grade'] +
            all_df_reset['Population 25 years and over - 9th to12th (No Diploma)']
    )

    all_df_reset['Sum Higher Education'] = (
            all_df_reset['Population 25 years and over - Graduate or Prefessional Degree'] +
            all_df_reset["Population 25 years and over - Bachelor's degree"] +
            all_df_reset["Population 25 years and over - Associate's degree"]
    )

    all_df_reset['Population 25 years and over - High School Graduate (and equivalent)'] = (all_df_reset[
                                                                                                'Percent Population 25 years and over - High School Graduate (and equivalent)'] / 100) * \
                                                                                           all_df_reset[
                                                                                               'Total population']
    all_df_reset['Population 25 years and over - Some college no degree'] = all_df_reset[
                                                                                "Percent Population 25 years and over - Some college, no degree"] / 100 * \
                                                                            all_df_reset['Total population']
    return all_df_reset


def calculate_education(all_df_reset):
    all_df_reset['Population 25 years and over - Less than 9th grade'] = (all_df_reset[
                                                                              'Percent Population 25 years and over - Less than 9th grade'] / 100) * \
                                                                         all_df_reset[
                                                                             'Total population']
    all_df_reset['Population 25 years and over - 9th to12th (No Diploma)'] = (all_df_reset[
                                                                                  'Percent Population 25 years and over - 9th to12th (No Diploma)'] / 100) * \
                                                                             all_df_reset[
                                                                                 'Total population']
    all_df_reset['Population 25 years and over - Graduate or Prefessional Degree'] = (all_df_reset[
                                                                                          'Percent Population 25 years and over - Graduate or Prefessional Degree'] / 100) * \
                                                                                     all_df_reset[
                                                                                         'Total population']
    all_df_reset["Population 25 years and over - Bachelor's degree"] = (all_df_reset[
                                                                            "Percent Population 25 years and over - Bachelor's degree"] / 100) * \
                                                                       all_df_reset[
                                                                           'Total population']
    all_df_reset["Population 25 years and over - Associate's degree"] = (all_df_reset[
                                                                             "Percent Population 25 years and over - Associate's degree"] / 100) * \
                                                                        all_df_reset[
                                                                            'Total population']
    return all_df_reset


def calculate_percentage_ages(df):
    df["Under 5 years"] = (df["Percent Under 5 years"] / 100) * df["Total population"]
    df["5 to 9 years"] = (df["Percent 5 to 9 years"] / 100) * df["Total population"]
    df["10 to 14 years"] = (df["Percent 10 to 14 years"] / 100) * df["Total population"]
    df["15 to 19 years"] = (df["Percent 15 to 19 years"] / 100) * df["Total population"]
    df["20 to 24 years"] = (df["Percent 20 to 24 years"] / 100) * df["Total population"]
    df["25 to 34 years"] = (df["Percent 25 to 34 years"] / 100) * df["Total population"]
    df["35 to 44 years"] = (df["Percent 35 to 44 years"] / 100) * df["Total population"]
    df["45 to 54 years"] = (df["Percent 45 to 54 years"] / 100) * df["Total population"]
    df["55 to 59 years"] = (df["Percent 55 to 59 years"] / 100) * df["Total population"]
    df["60 to 64 years"] = (df["Percent 60 to 64 years"] / 100) * df["Total population"]
    df["65 to 74 years"] = (df["Percent 65 to 74 years"] / 100) * df["Total population"]
    df["75 to 84 years"] = (df["Percent 75 to 84 years"] / 100) * df["Total population"]
    df["85 years and over"] = (df["Percent 85 years and over"] / 100) * df["Total population"]
    return df
