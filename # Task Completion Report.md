# Task Completion Report

## Task 1: Comparing Solar Potential Across Countries
### Objective
The goal was to synthesize cleaned datasets from Benin, Sierra Leone, and Togo to identify relative solar potential and key differences across countries. This involved:
- Loading cleaned datasets.
- Performing metric comparisons (GHI, DNI, DHI).
- Conducting statistical testing (ANOVA/Kruskal-Wallis).
- Summarizing key observations.
- Creating visual summaries.

### Actions Taken
1. **Data Loading**:
   - Cleaned datasets (`benin_clean.csv`, `sierra_leone_clean.csv`, `togo_clean.csv`) were loaded into a combined DataFrame.
   - A `Country` column was added to distinguish data from each country.

2. **Metric Comparison**:
   - Boxplots for GHI, DNI, and DHI were created to visualize distributions across countries.
   - A summary table was generated to compare mean, median, and standard deviation for each metric.

3. **Statistical Testing**:
   - Conducted a one-way ANOVA to assess whether differences in GHI between countries were statistically significant.
   - Performed a Kruskal-Wallis test as a non-parametric alternative.

4. **Key Observations**:
   - Added a markdown cell summarizing insights:
     - Benin shows the highest median GHI but also the greatest variability.
     - Sierra Leone has the lowest average DNI, indicating less direct solar radiation.
     - Togo demonstrates consistent solar potential with moderate variability.

5. **Visual Summary**:
   - Created a bar chart ranking countries by average GHI.

6. **GitHub Actions**:
   - Created a new branch `compare-countries` for this task.
   - Pushed the branch to the remote repository and opened a pull request for review.


