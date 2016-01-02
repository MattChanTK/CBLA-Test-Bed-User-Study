from scipy import stats

overall_interest = (6, 6, 6, 7, 9, 8, 7, 6, 7, 8)
responsiveness = (4, 5, 6, 6, 7, 8, 4.5, 6, 7, 9)
average_interest = (5.375, 2.875, 4.125, 5.9375, 5.375, 6.875, 4.625, 3.25, 5.125, 6.375)

correlation_1 = stats.pearsonr(overall_interest, responsiveness)
correlation_2 = stats.pearsonr(average_interest, responsiveness)
correlation_3 = stats.pearsonr(overall_interest, average_interest)

print(correlation_1)
print(correlation_2)
print(correlation_3)