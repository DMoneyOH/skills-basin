---
name: data-science-python
description: >
  "Fast in-memory DataFrame library for datasets that fit in RAM. Use when pandas is too slow but data still fits in memory. Lazy evaluation, parallel execution, Apache Arrow backend. Best for 1-100GB datasets, ETL pipelines, faster pandas replacement. For larger-than-RAM data use dask or vaex."
  Covers: data science python, matplotlib, seaborn, polars.
  Use for any task involving data science python, matplotlib, seaborn, polars.
merged_from:
  - matplotlib
  - seaborn
  - polars
merged_at: 2026-04-25
---

# data-science-python

<!-- matplotlib -->
## Overview

Matplotlib is Python's foundational visualization library for creating static, animated, and interactive plots. This skill provides guidance on using matplotlib effectively, covering both the pyplot interface (MATLAB-style) and the object-oriented API (Figure/Axes), along with best practices for creating publication-quality visualizations.

## When to Use This Skill

This skill should be used when:
- Creating any type of plot or chart (line, scatter, bar, histogram, heatmap, contour, etc.)
- Generating scientific or statistical visualizations
- Customizing plot appearance (colors, styles, labels, legends)
- Creating multi-panel figures with subplots
- Exporting visualizations to various formats (PNG, PDF, SVG, etc.)
- Building interactive plots or animations
- Working with 3D visualizations
- Integrating plots into Jupyter notebooks or GUI applications

## Core Concepts

### The Matplotlib Hierarchy

Matplotlib uses a hierarchical structure of objects:

1. **Figure** - The top-level container for all plot elements
2. **Axes** - The actual plotting area where data is displayed (one Figure can contain multiple Axes)
3. **Artist** - Everything visible on the figure (lines, text, ticks, etc.)
4. **Axis** - The number line objects (x-axis, y-axis) that handle ticks and labels

### Two Interfaces

**1. pyplot Interface (Implicit, MATLAB-style)**
```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```
- Convenient for quick, simple plots
- Maintains state automatically
- Good for interactive work and simple scripts

**2. Object-Oriented Interface (Explicit)**
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4])
ax.set_ylabel('some numbers')
plt.show()
```
- **Recommended for most use cases**
- More explicit control over figure and axes
- Better for complex figures with multiple subplots
- Easier to maintain and debug

## Common Workflows

### 1. Basic Plot Creation

**Single plot workflow:**
```python
import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes (OO interface - RECOMMENDED)
fig, ax = plt.subplots(figsize=(10, 6))

# Generate and plot data
x = np.linspace(0, 2*np.pi, 100)
ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')

# Customize
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Trigonometric Functions')
ax.legend()
ax.grid(True, alpha=0.3)

# Save and/or display
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()
```

### 2. Multiple Subplots

**Creating subplot layouts:**
```python
# Method 1: Regular grid
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y1)
axes[0, 1].scatter(x, y2)
axes[1, 0].bar(categories, values)
axes[1, 1].hist(data, bins=30)

# Method 2: Mosaic layout (more flexible)
fig, axes = plt.subplot_mosaic([['left', 'right_top'],
                                 ['left', 'right_bottom']],
                                figsize=(10, 8))
axes['left'].plot(x, y)
axes['right_top'].scatter(x, y)
axes['right_bottom'].hist(data)

# Method 3: GridSpec (maximum control)
from matplotlib.gridspec import GridSpec
fig = plt.figure(figsize=(12, 8))
gs = GridSpec(3, 3, figure=fig)
ax1 = fig.add_subplot(gs[0, :])  # Top row, all columns
ax2 = fig.add_subplot(gs[1:, 0])  # Bottom two rows, first column
ax3 = fig.add_subplot(gs[1:, 1:])  # Bottom two rows, last two columns
```

### 3. Plot Types and Use Cases

**Line plots** - Time series, continuous data, trends
```python
ax.plot(x, y, linewidth=2, linestyle='--', marker='o', color='blue')
```

**Scatter plots** - Relationships between variables, correlations
```python
ax.scatter(x, y, s=sizes, c=colors, alpha=0.6, cmap='viridis')
```

**Bar charts** - Categorical comparisons
```python
ax.bar(categories, values, color='steelblue', edgecolor='black')
# For horizontal bars:
ax.barh(categories, values)
```

**Histograms** - Distributions
```python
ax.hist(data, bins=30, edgecolor='black', alpha=0.7)
```

**Heatmaps** - Matrix data, correlations
```python
im = ax.imshow(matrix, cmap='coolwarm', aspect='auto')
plt.colorbar(im, ax=ax)
```

**Contour plots** - 3D data on 2D plane
```python
contour = ax.contour(X, Y, Z, levels=10)
ax.clabel(contour, inline=True, fontsize=8)
```

**Box plots** - Statistical distributions
```python
ax.boxplot([data1, data2, data3], labels=['A', 'B', 'C'])
```

**Violin plots** - Distribution densities
```python
ax.violinplot([data1, data2, data3], positions=[1, 2, 3])
```

For comprehensive plot type examples and variations, refer to `references/plot_types.md`.

### 4. Styling and Customization

**Color specification methods:**
- Named colors: `'red'`, `'blue'`, `'steelblue'`
- Hex codes: `'#FF5733'`
- RGB tuples: `(0.1, 0.2, 0.3)`
- Colormaps: `cmap='viridis'`, `cmap='plasma'`, `cmap='coolwarm'`

**Using style sheets:**
```python
plt.style.use('seaborn-v0_8-darkgrid')  # Apply predefined style
# Available styles: 'ggplot', 'bmh', 'fivethirtyeight', etc.
print(plt.style.available)  # List all available styles
```

**Customizing with rcParams:**
```python
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.titlesize'] = 18
```

**Text and annotations:**
```python
ax.text(x, y, 'annotation', fontsize=12, ha='center')
ax.annotate('important point', xy=(x, y), xytext=(x+1, y+1),
            arrowprops=dict(arrowstyle='->', color='red'))
```

For detailed styling options and colormap guidelines, see `references/styling_guide.md`.

### 5. Saving Figures

**Export to various formats:**
```python
# High-resolution PNG for presentations/papers
plt.savefig('figure.png', dpi=300, bbox_inches='tight', facecolor='white')

# Vector format for publications (scalable)
plt.savefig('figure.pdf', bbox_inches='tight')
plt.savefig('figure.svg', bbox_inches='tight')

# Transparent background
plt.savefig('figure.png', dpi=300, bbox_inches='tight', transparent=True)
```

**Important parameters:**
- `dpi`: Resolution (300 for publications, 150 for web, 72 for screen)
- `bbox_inches='tight'`: Removes excess whitespace
- `facecolor='white'`: Ensures white background (useful for transparent themes)
- `transparent=True`: Transparent background

### 6. Working with 3D Plots

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
ax.plot_surface(X, Y, Z, cmap='viridis')

# 3D scatter
ax.scatter(x, y, z, c=colors, marker='o')

# 3D line plot
ax.plot(x, y, z, linewidth=2)

# Labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
```

## Best Practices

### 1. Interface Selection
- **Use the object-oriented interface** (fig, ax = plt.subplots()) for production code
- Reserve pyplot interface for quick interactive exploration only
- Always create figures explicitly rather than relying on implicit state

### 2. Figure Size and DPI
- Set figsize at creation: `fig, ax = plt.subplots(figsize=(10, 6))`
- Use appropriate DPI for output medium:
  - Screen/notebook: 72-100 dpi
  - Web: 150 dpi
  - Print/publications: 300 dpi

### 3. Layout Management
- Use `constrained_layout=True` or `tight_layout()` to prevent overlapping elements
- `fig, ax = plt.subplots(constrained_layout=True)` is recommended for automatic spacing

### 4. Colormap Selection
- **Sequential** (viridis, plasma, inferno): Ordered data with consistent progression
- **Diverging** (coolwarm, RdBu): Data with meaningful center point (e.g., zero)
- **Qualitative** (tab10, Set3): Categorical/nominal data
- Avoid rainbow colormaps (jet) - they are not perceptually uniform

### 5. Accessibility
- Use colorblind-friendly colormaps (viridis, cividis)
- Add patterns/hatching for bar charts in addition to colors
- Ensure sufficient contrast between elements
- Include descriptive labels and legends

### 6. Performance
- For large datasets, use `rasterized=True` in plot calls to reduce file size
- Use appropriate data reduction before plotting (e.g., downsample dense time series)
- For animations, use blitting for better performance

### 7. Code Organization
```python
# Good practice: Clear structure
def create_analysis_plot(data, title):
    """Create standardized analysis plot."""
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)

    # Plot data
    ax.plot(data['x'], data['y'], linewidth=2)

    # Customize
    ax.set_xlabel('X Axis Label', fontsize=12)
    ax.set_ylabel('Y Axis Label', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    return fig, ax

# Use the function
fig, ax = create_analysis_plot(my_data, 'My Analysis')
plt.savefig('analysis.png', dpi=300, bbox_inches='tight')
```

## Quick Reference Scripts

This skill includes helper scripts in the `scripts/` directory:

### `plot_template.py`
Template script demonstrating various plot types with best practices. Use this as a starting point for creating new visualizations.

**Usage:**
```bash
python scripts/plot_template.py
```

### `style_configurator.py`
Interactive utility to configure matplotlib style preferences and generate custom style sheets.

**Usage:**
```bash
python scripts/style_configurator.py
```

## Detailed References

For comprehensive information, consult the reference documents:

- **`references/plot_types.md`** - Complete catalog of plot types with code examples and use cases
- **`references/styling_guide.md`** - Detailed styling options, colormaps, and customization
- **`references/api_reference.md`** - Core classes and methods reference
- **`references/common_issues.md`** - Troubleshooting guide for common problems

## Integration with Other Tools

Matplotlib integrates well with:
- **NumPy/Pandas** - Direct plotting from arrays and DataFrames
- **Seaborn** - High-level statistical visualizations built on matplotlib
- **Jupyter** - Interactive plotting with `%matplotlib inline` or `%matplotlib widget`
- **GUI frameworks** - Embedding in Tkinter, Qt, wxPython applications

## Common Gotchas

1. **Overlapping elements**: Use `constrained_layout=True` or `tight_layout()`
2. **State confusion**: Use OO interface to avoid pyplot state machine issues
3. **Memory issues with many figures**: Close figures explicitly with `plt.close(fig)`
4. **Font warnings**: Install fonts or suppress warnings with `plt.rcParams['font.sans-serif']`
5. **DPI confusion**: Remember that figsize is in inches, not pixels: `pixels = dpi * inches`

## Additional Resources

- Official documentation: https://matplotlib.org/
- Gallery: https://matplotlib.org/stable/gallery/index.html
- Cheatsheets: https://matplotlib.org/cheatsheets/
- Tutorials: https://matplotlib.org/stable/tutorials/index.html



<!-- MERGED INTO: data-science-python on 2026-04-18 -->
<!-- Use `data-science-python` instead. -->

---

<!-- seaborn -->
BSD-3-Clause license
metadata:
    skill-author: K-Dense Inc.
---

# Seaborn Statistical Visualization

## Overview

Seaborn is a Python visualization library for creating publication-quality statistical graphics. Use this skill for dataset-oriented plotting, multivariate analysis, automatic statistical estimation, and complex multi-panel figures with minimal code.

## Design Philosophy

Seaborn follows these core principles:

1. **Dataset-oriented**: Work directly with DataFrames and named variables rather than abstract coordinates
2. **Semantic mapping**: Automatically translate data values into visual properties (colors, sizes, styles)
3. **Statistical awareness**: Built-in aggregation, error estimation, and confidence intervals
4. **Aesthetic defaults**: Publication-ready themes and color palettes out of the box
5. **Matplotlib integration**: Full compatibility with matplotlib customization when needed

## Quick Start

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load example dataset
df = sns.load_dataset('tips')

# Create a simple visualization
sns.scatterplot(data=df, x='total_bill', y='tip', hue='day')
plt.show()
```

## Core Plotting Interfaces

### Function Interface (Traditional)

The function interface provides specialized plotting functions organized by visualization type. Each category has **axes-level** functions (plot to single axes) and **figure-level** functions (manage entire figure with faceting).

**When to use:**
- Quick exploratory analysis
- Single-purpose visualizations
- When you need a specific plot type

### Objects Interface (Modern)

The `seaborn.objects` interface provides a declarative, composable API similar to ggplot2. Build visualizations by chaining methods to specify data mappings, marks, transformations, and scales.

**When to use:**
- Complex layered visualizations
- When you need fine-grained control over transformations
- Building custom plot types
- Programmatic plot generation

```python
from seaborn import objects as so

# Declarative syntax
(
    so.Plot(data=df, x='total_bill', y='tip')
    .add(so.Dot(), color='day')
    .add(so.Line(), so.PolyFit())
)
```

## Plotting Functions by Category

### Relational Plots (Relationships Between Variables)

**Use for:** Exploring how two or more variables relate to each other

- `scatterplot()` - Display individual observations as points
- `lineplot()` - Show trends and changes (automatically aggregates and computes CI)
- `relplot()` - Figure-level interface with automatic faceting

**Key parameters:**
- `x`, `y` - Primary variables
- `hue` - Color encoding for additional categorical/continuous variable
- `size` - Point/line size encoding
- `style` - Marker/line style encoding
- `col`, `row` - Facet into multiple subplots (figure-level only)

```python
# Scatter with multiple semantic mappings
sns.scatterplot(data=df, x='total_bill', y='tip',
                hue='time', size='size', style='sex')

# Line plot with confidence intervals
sns.lineplot(data=timeseries, x='date', y='value', hue='category')

# Faceted relational plot
sns.relplot(data=df, x='total_bill', y='tip',
            col='time', row='sex', hue='smoker', kind='scatter')
```

### Distribution Plots (Single and Bivariate Distributions)

**Use for:** Understanding data spread, shape, and probability density

- `histplot()` - Bar-based frequency distributions with flexible binning
- `kdeplot()` - Smooth density estimates using Gaussian kernels
- `ecdfplot()` - Empirical cumulative distribution (no parameters to tune)
- `rugplot()` - Individual observation tick marks
- `displot()` - Figure-level interface for univariate and bivariate distributions
- `jointplot()` - Bivariate plot with marginal distributions
- `pairplot()` - Matrix of pairwise relationships across dataset

**Key parameters:**
- `x`, `y` - Variables (y optional for univariate)
- `hue` - Separate distributions by category
- `stat` - Normalization: "count", "frequency", "probability", "density"
- `bins` / `binwidth` - Histogram binning control
- `bw_adjust` - KDE bandwidth multiplier (higher = smoother)
- `fill` - Fill area under curve
- `multiple` - How to handle hue: "layer", "stack", "dodge", "fill"

```python
# Histogram with density normalization
sns.histplot(data=df, x='total_bill', hue='time',
             stat='density', multiple='stack')

# Bivariate KDE with contours
sns.kdeplot(data=df, x='total_bill', y='tip',
            fill=True, levels=5, thresh=0.1)

# Joint plot with marginals
sns.jointplot(data=df, x='total_bill', y='tip',
              kind='scatter', hue='time')

# Pairwise relationships
sns.pairplot(data=df, hue='species', corner=True)
```

### Categorical Plots (Comparisons Across Categories)

**Use for:** Comparing distributions or statistics across discrete categories

**Categorical scatterplots:**
- `stripplot()` - Points with jitter to show all observations
- `swarmplot()` - Non-overlapping points (beeswarm algorithm)

**Distribution comparisons:**
- `boxplot()` - Quartiles and outliers
- `violinplot()` - KDE + quartile information
- `boxenplot()` - Enhanced boxplot for larger datasets

**Statistical estimates:**
- `barplot()` - Mean/aggregate with confidence intervals
- `pointplot()` - Point estimates with connecting lines
- `countplot()` - Count of observations per category

**Figure-level:**
- `catplot()` - Faceted categorical plots (set `kind` parameter)

**Key parameters:**
- `x`, `y` - Variables (one typically categorical)
- `hue` - Additional categorical grouping
- `order`, `hue_order` - Control category ordering
- `dodge` - Separate hue levels side-by-side
- `orient` - "v" (vertical) or "h" (horizontal)
- `kind` - Plot type for catplot: "strip", "swarm", "box", "violin", "bar", "point"

```python
# Swarm plot showing all points
sns.swarmplot(data=df, x='day', y='total_bill', hue='sex')

# Violin plot with split for comparison
sns.violinplot(data=df, x='day', y='total_bill',
               hue='sex', split=True)

# Bar plot with error bars
sns.barplot(data=df, x='day', y='total_bill',
            hue='sex', estimator='mean', errorbar='ci')

# Faceted categorical plot
sns.catplot(data=df, x='day', y='total_bill',
            col='time', kind='box')
```

### Regression Plots (Linear Relationships)

**Use for:** Visualizing linear regressions and residuals

- `regplot()` - Axes-level regression plot with scatter + fit line
- `lmplot()` - Figure-level with faceting support
- `residplot()` - Residual plot for assessing model fit

**Key parameters:**
- `x`, `y` - Variables to regress
- `order` - Polynomial regression order
- `logistic` - Fit logistic regression
- `robust` - Use robust regression (less sensitive to outliers)
- `ci` - Confidence interval width (default 95)
- `scatter_kws`, `line_kws` - Customize scatter and line properties

```python
# Simple linear regression
sns.regplot(data=df, x='total_bill', y='tip')

# Polynomial regression with faceting
sns.lmplot(data=df, x='total_bill', y='tip',
           col='time', order=2, ci=95)

# Check residuals
sns.residplot(data=df, x='total_bill', y='tip')
```

### Matrix Plots (Rectangular Data)

**Use for:** Visualizing matrices, correlations, and grid-structured data

- `heatmap()` - Color-encoded matrix with annotations
- `clustermap()` - Hierarchically-clustered heatmap

**Key parameters:**
- `data` - 2D rectangular dataset (DataFrame or array)
- `annot` - Display values in cells
- `fmt` - Format string for annotations (e.g., ".2f")
- `cmap` - Colormap name
- `center` - Value at colormap center (for diverging colormaps)
- `vmin`, `vmax` - Color scale limits
- `square` - Force square cells
- `linewidths` - Gap between cells

```python
# Correlation heatmap
corr = df.corr()
sns.heatmap(corr, annot=True, fmt='.2f',
            cmap='coolwarm', center=0, square=True)

# Clustered heatmap
sns.clustermap(data, cmap='viridis',
               standard_scale=1, figsize=(10, 10))
```

## Multi-Plot Grids

Seaborn provides grid objects for creating complex multi-panel figures:

### FacetGrid

Create subplots based on categorical variables. Most useful when called through figure-level functions (`relplot`, `displot`, `catplot`), but can be used directly for custom plots.

```python
g = sns.FacetGrid(df, col='time', row='sex', hue='smoker')
g.map(sns.scatterplot, 'total_bill', 'tip')
g.add_legend()
```

### PairGrid

Show pairwise relationships between all variables in a dataset.

```python
g = sns.PairGrid(df, hue='species')
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot)
g.add_legend()
```

### JointGrid

Combine bivariate plot with marginal distributions.

```python
g = sns.JointGrid(data=df, x='total_bill', y='tip')
g.plot_joint(sns.scatterplot)
g.plot_marginals(sns.histplot)
```

## Figure-Level vs Axes-Level Functions

Understanding this distinction is crucial for effective seaborn usage:

### Axes-Level Functions
- Plot to a single matplotlib `Axes` object
- Integrate easily into complex matplotlib figures
- Accept `ax=` parameter for precise placement
- Return `Axes` object
- Examples: `scatterplot`, `histplot`, `boxplot`, `regplot`, `heatmap`

**When to use:**
- Building custom multi-plot layouts
- Combining different plot types
- Need matplotlib-level control
- Integrating with existing matplotlib code

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
sns.scatterplot(data=df, x='x', y='y', ax=axes[0, 0])
sns.histplot(data=df, x='x', ax=axes[0, 1])
sns.boxplot(data=df, x='cat', y='y', ax=axes[1, 0])
sns.kdeplot(data=df, x='x', y='y', ax=axes[1, 1])
```

### Figure-Level Functions
- Manage entire figure including all subplots
- Built-in faceting via `col` and `row` parameters
- Return `FacetGrid`, `JointGrid`, or `PairGrid` objects
- Use `height` and `aspect` for sizing (per subplot)
- Cannot be placed in existing figure
- Examples: `relplot`, `displot`, `catplot`, `lmplot`, `jointplot`, `pairplot`

**When to use:**
- Faceted visualizations (small multiples)
- Quick exploratory analysis
- Consistent multi-panel layouts
- Don't need to combine with other plot types

```python
# Automatic faceting
sns.relplot(data=df, x='x', y='y', col='category', row='group',
            hue='type', height=3, aspect=1.2)
```

## Data Structure Requirements

### Long-Form Data (Preferred)

Each variable is a column, each observation is a row. This "tidy" format provides maximum flexibility:

```python
# Long-form structure
   subject  condition  measurement
0        1    control         10.5
1        1  treatment         12.3
2        2    control          9.8
3        2  treatment         13.1
```

**Advantages:**
- Works with all seaborn functions
- Easy to remap variables to visual properties
- Supports arbitrary complexity
- Natural for DataFrame operations

### Wide-Form Data

Variables are spread across columns. Useful for simple rectangular data:

```python
# Wide-form structure
   control  treatment
0     10.5       12.3
1      9.8       13.1
```

**Use cases:**
- Simple time series
- Correlation matrices
- Heatmaps
- Quick plots of array data

**Converting wide to long:**
```python
df_long = df.melt(var_name='condition', value_name='measurement')
```

## Color Palettes

Seaborn provides carefully designed color palettes for different data types:

### Qualitative Palettes (Categorical Data)

Distinguish categories through hue variation:
- `"deep"` - Default, vivid colors
- `"muted"` - Softer, less saturated
- `"pastel"` - Light, desaturated
- `"bright"` - Highly saturated
- `"dark"` - Dark values
- `"colorblind"` - Safe for color vision deficiency

```python
sns.set_palette("colorblind")
sns.color_palette("Set2")
```

### Sequential Palettes (Ordered Data)

Show progression from low to high values:
- `"rocket"`, `"mako"` - Wide luminance range (good for heatmaps)
- `"flare"`, `"crest"` - Restricted luminance (good for points/lines)
- `"viridis"`, `"magma"`, `"plasma"` - Matplotlib perceptually uniform

```python
sns.heatmap(data, cmap='rocket')
sns.kdeplot(data=df, x='x', y='y', cmap='mako', fill=True)
```

### Diverging Palettes (Centered Data)

Emphasize deviations from a midpoint:
- `"vlag"` - Blue to red
- `"icefire"` - Blue to orange
- `"coolwarm"` - Cool to warm
- `"Spectral"` - Rainbow diverging

```python
sns.heatmap(correlation_matrix, cmap='vlag', center=0)
```

### Custom Palettes

```python
# Create custom palette
custom = sns.color_palette("husl", 8)

# Light to dark gradient
palette = sns.light_palette("seagreen", as_cmap=True)

# Diverging palette from hues
palette = sns.diverging_palette(250, 10, as_cmap=True)
```

## Theming and Aesthetics

### Set Theme

`set_theme()` controls overall appearance:

```python
# Set complete theme
sns.set_theme(style='whitegrid', palette='pastel', font='sans-serif')

# Reset to defaults
sns.set_theme()
```

### Styles

Control background and grid appearance:
- `"darkgrid"` - Gray background with white grid (default)
- `"whitegrid"` - White background with gray grid
- `"dark"` - Gray background, no grid
- `"white"` - White background, no grid
- `"ticks"` - White background with axis ticks

```python
sns.set_style("whitegrid")

# Remove spines
sns.despine(left=False, bottom=False, offset=10, trim=True)

# Temporary style
with sns.axes_style("white"):
    sns.scatterplot(data=df, x='x', y='y')
```

### Contexts

Scale elements for different use cases:
- `"paper"` - Smallest (default)
- `"notebook"` - Slightly larger
- `"talk"` - Presentation slides
- `"poster"` - Large format

```python
sns.set_context("talk", font_scale=1.2)

# Temporary context
with sns.plotting_context("poster"):
    sns.barplot(data=df, x='category', y='value')
```

## Best Practices

### 1. Data Preparation

Always use well-structured DataFrames with meaningful column names:

```python
# Good: Named columns in DataFrame
df = pd.DataFrame({'bill': bills, 'tip': tips, 'day': days})
sns.scatterplot(data=df, x='bill', y='tip', hue='day')

# Avoid: Unnamed arrays
sns.scatterplot(x=x_array, y=y_array)  # Loses axis labels
```

### 2. Choose the Right Plot Type

**Continuous x, continuous y:** `scatterplot`, `lineplot`, `kdeplot`, `regplot`
**Continuous x, categorical y:** `violinplot`, `boxplot`, `stripplot`, `swarmplot`
**One continuous variable:** `histplot`, `kdeplot`, `ecdfplot`
**Correlations/matrices:** `heatmap`, `clustermap`
**Pairwise relationships:** `pairplot`, `jointplot`

### 3. Use Figure-Level Functions for Faceting

```python
# Instead of manual subplot creation
sns.relplot(data=df, x='x', y='y', col='category', col_wrap=3)

# Not: Creating subplots manually for simple faceting
```

### 4. Leverage Semantic Mappings

Use `hue`, `size`, and `style` to encode additional dimensions:

```python
sns.scatterplot(data=df, x='x', y='y',
                hue='category',      # Color by category
                size='importance',    # Size by continuous variable
                style='type')         # Marker style by type
```

### 5. Control Statistical Estimation

Many functions compute statistics automatically. Understand and customize:

```python
# Lineplot computes mean and 95% CI by default
sns.lineplot(data=df, x='time', y='value',
             errorbar='sd')  # Use standard deviation instead

# Barplot computes mean by default
sns.barplot(data=df, x='category', y='value',
            estimator='median',  # Use median instead
            errorbar=('ci', 95))  # Bootstrapped CI
```

### 6. Combine with Matplotlib

Seaborn integrates seamlessly with matplotlib for fine-tuning:

```python
ax = sns.scatterplot(data=df, x='x', y='y')
ax.set(xlabel='Custom X Label', ylabel='Custom Y Label',
       title='Custom Title')
ax.axhline(y=0, color='r', linestyle='--')
plt.tight_layout()
```

### 7. Save High-Quality Figures

```python
fig = sns.relplot(data=df, x='x', y='y', col='group')
fig.savefig('figure.png', dpi=300, bbox_inches='tight')
fig.savefig('figure.pdf')  # Vector format for publications
```

## Common Patterns

### Exploratory Data Analysis

```python
# Quick overview of all relationships
sns.pairplot(data=df, hue='target', corner=True)

# Distribution exploration
sns.displot(data=df, x='variable', hue='group',
            kind='kde', fill=True, col='category')

# Correlation analysis
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
```

### Publication-Quality Figures

```python
sns.set_theme(style='ticks', context='paper', font_scale=1.1)

g = sns.catplot(data=df, x='treatment', y='response',
                col='cell_line', kind='box', height=3, aspect=1.2)
g.set_axis_labels('Treatment Condition', 'Response (μM)')
g.set_titles('{col_name}')
sns.despine(trim=True)

g.savefig('figure.pdf', dpi=300, bbox_inches='tight')
```

### Complex Multi-Panel Figures

```python
# Using matplotlib subplots with seaborn
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.scatterplot(data=df, x='x1', y='y', hue='group', ax=axes[0, 0])
sns.histplot(data=df, x='x1', hue='group', ax=axes[0, 1])
sns.violinplot(data=df, x='group', y='y', ax=axes[1, 0])
sns.heatmap(df.pivot_table(values='y', index='x1', columns='x2'),
            ax=axes[1, 1], cmap='viridis')

plt.tight_layout()
```

### Time Series with Confidence Bands

```python
# Lineplot automatically aggregates and shows CI
sns.lineplot(data=timeseries, x='date', y='measurement',
             hue='sensor', style='location', errorbar='sd')

# For more control
g = sns.relplot(data=timeseries, x='date', y='measurement',
                col='location', hue='sensor', kind='line',
                height=4, aspect=1.5, errorbar=('ci', 95))
g.set_axis_labels('Date', 'Measurement (units)')
```

## Troubleshooting

### Issue: Legend Outside Plot Area

Figure-level functions place legends outside by default. To move inside:

```python
g = sns.relplot(data=df, x='x', y='y', hue='category')
g._legend.set_bbox_to_anchor((0.9, 0.5))  # Adjust position
```

### Issue: Overlapping Labels

```python
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
```

### Issue: Figure Too Small

For figure-level functions:
```python
sns.relplot(data=df, x='x', y='y', height=6, aspect=1.5)
```

For axes-level functions:
```python
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='x', y='y', ax=ax)
```

### Issue: Colors Not Distinct Enough

```python
# Use a different palette
sns.set_palette("bright")

# Or specify number of colors
palette = sns.color_palette("husl", n_colors=len(df['category'].unique()))
sns.scatterplot(data=df, x='x', y='y', hue='category', palette=palette)
```

### Issue: KDE Too Smooth or Jagged

```python
# Adjust bandwidth
sns.kdeplot(data=df, x='x', bw_adjust=0.5)  # Less smooth
sns.kdeplot(data=df, x='x', bw_adjust=2)    # More smooth
```

## Resources

This skill includes reference materials for deeper exploration:

### references/

- `function_reference.md` - Comprehensive listing of all seaborn functions with parameters and examples
- `objects_interface.md` - Detailed guide to the modern seaborn.objects API
- `examples.md` - Common use cases and code patterns for different analysis scenarios

Load reference files as needed for detailed function signatures, advanced parameters, or specific examples.



<!-- MERGED INTO: data-science-python on 2026-04-18 -->
<!-- Use `data-science-python` instead. -->

---

<!-- polars -->
## Overview

Polars is a lightning-fast DataFrame library for Python and Rust built on Apache Arrow. Work with Polars' expression-based API, lazy evaluation framework, and high-performance data manipulation capabilities for efficient data processing, pandas migration, and data pipeline optimization.

## Quick Start

### Installation and Basic Usage

Install Polars:
```python
uv pip install polars
```

Basic DataFrame creation and operations:
```python
import polars as pl

# Create DataFrame
df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["NY", "LA", "SF"]
})

# Select columns
df.select("name", "age")

# Filter rows
df.filter(pl.col("age") > 25)

# Add computed columns
df.with_columns(
    age_plus_10=pl.col("age") + 10
)
```

## Core Concepts

### Expressions

Expressions are the fundamental building blocks of Polars operations. They describe transformations on data and can be composed, reused, and optimized.

**Key principles:**
- Use `pl.col("column_name")` to reference columns
- Chain methods to build complex transformations
- Expressions are lazy and only execute within contexts (select, with_columns, filter, group_by)

**Example:**
```python
# Expression-based computation
df.select(
    pl.col("name"),
    (pl.col("age") * 12).alias("age_in_months")
)
```

### Lazy vs Eager Evaluation

**Eager (DataFrame):** Operations execute immediately
```python
df = pl.read_csv("file.csv")  # Reads immediately
result = df.filter(pl.col("age") > 25)  # Executes immediately
```

**Lazy (LazyFrame):** Operations build a query plan, optimized before execution
```python
lf = pl.scan_csv("file.csv")  # Doesn't read yet
result = lf.filter(pl.col("age") > 25).select("name", "age")
df = result.collect()  # Now executes optimized query
```

**When to use lazy:**
- Working with large datasets
- Complex query pipelines
- When only some columns/rows are needed
- Performance is critical

**Benefits of lazy evaluation:**
- Automatic query optimization
- Predicate pushdown
- Projection pushdown
- Parallel execution

For detailed concepts, load `references/core_concepts.md`.

## Common Operations

### Select
Select and manipulate columns:
```python
# Select specific columns
df.select("name", "age")

# Select with expressions
df.select(
    pl.col("name"),
    (pl.col("age") * 2).alias("double_age")
)

# Select all columns matching a pattern
df.select(pl.col("^.*_id$"))
```

### Filter
Filter rows by conditions:
```python
# Single condition
df.filter(pl.col("age") > 25)

# Multiple conditions (cleaner than using &)
df.filter(
    pl.col("age") > 25,
    pl.col("city") == "NY"
)

# Complex conditions
df.filter(
    (pl.col("age") > 25) | (pl.col("city") == "LA")
)
```

### With Columns
Add or modify columns while preserving existing ones:
```python
# Add new columns
df.with_columns(
    age_plus_10=pl.col("age") + 10,
    name_upper=pl.col("name").str.to_uppercase()
)

# Parallel computation (all columns computed in parallel)
df.with_columns(
    pl.col("value") * 10,
    pl.col("value") * 100,
)
```

### Group By and Aggregations
Group data and compute aggregations:
```python
# Basic grouping
df.group_by("city").agg(
    pl.col("age").mean().alias("avg_age"),
    pl.len().alias("count")
)

# Multiple group keys
df.group_by("city", "department").agg(
    pl.col("salary").sum()
)

# Conditional aggregations
df.group_by("city").agg(
    (pl.col("age") > 30).sum().alias("over_30")
)
```

For detailed operation patterns, load `references/operations.md`.

## Aggregations and Window Functions

### Aggregation Functions
Common aggregations within `group_by` context:
- `pl.len()` - count rows
- `pl.col("x").sum()` - sum values
- `pl.col("x").mean()` - average
- `pl.col("x").min()` / `pl.col("x").max()` - extremes
- `pl.first()` / `pl.last()` - first/last values

### Window Functions with `over()`
Apply aggregations while preserving row count:
```python
# Add group statistics to each row
df.with_columns(
    avg_age_by_city=pl.col("age").mean().over("city"),
    rank_in_city=pl.col("salary").rank().over("city")
)

# Multiple grouping columns
df.with_columns(
    group_avg=pl.col("value").mean().over("category", "region")
)
```

**Mapping strategies:**
- `group_to_rows` (default): Preserves original row order
- `explode`: Faster but groups rows together
- `join`: Creates list columns

## Data I/O

### Supported Formats
Polars supports reading and writing:
- CSV, Parquet, JSON, Excel
- Databases (via connectors)
- Cloud storage (S3, Azure, GCS)
- Google BigQuery
- Multiple/partitioned files

### Common I/O Operations

**CSV:**
```python
# Eager
df = pl.read_csv("file.csv")
df.write_csv("output.csv")

# Lazy (preferred for large files)
lf = pl.scan_csv("file.csv")
result = lf.filter(...).select(...).collect()
```

**Parquet (recommended for performance):**
```python
df = pl.read_parquet("file.parquet")
df.write_parquet("output.parquet")
```

**JSON:**
```python
df = pl.read_json("file.json")
df.write_json("output.json")
```

For comprehensive I/O documentation, load `references/io_guide.md`.

## Transformations

### Joins
Combine DataFrames:
```python
# Inner join
df1.join(df2, on="id", how="inner")

# Left join
df1.join(df2, on="id", how="left")

# Join on different column names
df1.join(df2, left_on="user_id", right_on="id")
```

### Concatenation
Stack DataFrames:
```python
# Vertical (stack rows)
pl.concat([df1, df2], how="vertical")

# Horizontal (add columns)
pl.concat([df1, df2], how="horizontal")

# Diagonal (union with different schemas)
pl.concat([df1, df2], how="diagonal")
```

### Pivot and Unpivot
Reshape data:
```python
# Pivot (wide format)
df.pivot(values="sales", index="date", columns="product")

# Unpivot (long format)
df.unpivot(index="id", on=["col1", "col2"])
```

For detailed transformation examples, load `references/transformations.md`.

## Pandas Migration

Polars offers significant performance improvements over pandas with a cleaner API. Key differences:

### Conceptual Differences
- **No index**: Polars uses integer positions only
- **Strict typing**: No silent type conversions
- **Lazy evaluation**: Available via LazyFrame
- **Parallel by default**: Operations parallelized automatically

### Common Operation Mappings

| Operation | Pandas | Polars |
|-----------|--------|--------|
| Select column | `df["col"]` | `df.select("col")` |
| Filter | `df[df["col"] > 10]` | `df.filter(pl.col("col") > 10)` |
| Add column | `df.assign(x=...)` | `df.with_columns(x=...)` |
| Group by | `df.groupby("col").agg(...)` | `df.group_by("col").agg(...)` |
| Window | `df.groupby("col").transform(...)` | `df.with_columns(...).over("col")` |

### Key Syntax Patterns

**Pandas sequential (slow):**
```python
df.assign(
    col_a=lambda df_: df_.value * 10,
    col_b=lambda df_: df_.value * 100
)
```

**Polars parallel (fast):**
```python
df.with_columns(
    col_a=pl.col("value") * 10,
    col_b=pl.col("value") * 100,
)
```

For comprehensive migration guide, load `references/pandas_migration.md`.

## Best Practices

### Performance Optimization

1. **Use lazy evaluation for large datasets:**
   ```python
   lf = pl.scan_csv("large.csv")  # Don't use read_csv
   result = lf.filter(...).select(...).collect()
   ```

2. **Avoid Python functions in hot paths:**
   - Stay within expression API for parallelization
   - Use `.map_elements()` only when necessary
   - Prefer native Polars operations

3. **Use streaming for very large data:**
   ```python
   lf.collect(streaming=True)
   ```

4. **Select only needed columns early:**
   ```python
   # Good: Select columns early
   lf.select("col1", "col2").filter(...)

   # Bad: Filter on all columns first
   lf.filter(...).select("col1", "col2")
   ```

5. **Use appropriate data types:**
   - Categorical for low-cardinality strings
   - Appropriate integer sizes (i32 vs i64)
   - Date types for temporal data

### Expression Patterns

**Conditional operations:**
```python
pl.when(condition).then(value).otherwise(other_value)
```

**Column operations across multiple columns:**
```python
df.select(pl.col("^.*_value$") * 2)  # Regex pattern
```

**Null handling:**
```python
pl.col("x").fill_null(0)
pl.col("x").is_null()
pl.col("x").drop_nulls()
```

For additional best practices and patterns, load `references/best_practices.md`.

## Resources

This skill includes comprehensive reference documentation:

### references/
- `core_concepts.md` - Detailed explanations of expressions, lazy evaluation, and type system
- `operations.md` - Comprehensive guide to all common operations with examples
- `pandas_migration.md` - Complete migration guide from pandas to Polars
- `io_guide.md` - Data I/O operations for all supported formats
- `transformations.md` - Joins, concatenation, pivots, and reshaping operations
- `best_practices.md` - Performance optimization tips and common patterns

Load these references as needed when users require detailed information about specific topics.



<!-- MERGED INTO: data-science-python on 2026-04-18 -->
<!-- Use `data-science-python` instead. -->

---

<!-- statsmodels -->
## Overview

Statsmodels is Python's premier library for statistical modeling, providing tools for estimation, inference, and diagnostics across a wide range of statistical methods. Apply this skill for rigorous statistical analysis, from simple linear regression to complex time series models and econometric analyses.

## When to Use This Skill

This skill should be used when:
- Fitting regression models (OLS, WLS, GLS, quantile regression)
- Performing generalized linear modeling (logistic, Poisson, Gamma, etc.)
- Analyzing discrete outcomes (binary, multinomial, count, ordinal)
- Conducting time series analysis (ARIMA, SARIMAX, VAR, forecasting)
- Running statistical tests and diagnostics
- Testing model assumptions (heteroskedasticity, autocorrelation, normality)
- Detecting outliers and influential observations
- Comparing models (AIC/BIC, likelihood ratio tests)
- Estimating causal effects
- Producing publication-ready statistical tables and inference

## Quick Start Guide

### Linear Regression (OLS)

```python
import statsmodels.api as sm
import numpy as np
import pandas as pd

# Prepare data - ALWAYS add constant for intercept
X = sm.add_constant(X_data)

# Fit OLS model
model = sm.OLS(y, X)
results = model.fit()

# View comprehensive results
print(results.summary())

# Key results
print(f"R-squared: {results.rsquared:.4f}")
print(f"Coefficients:\\n{results.params}")
print(f"P-values:\\n{results.pvalues}")

# Predictions with confidence intervals
predictions = results.get_prediction(X_new)
pred_summary = predictions.summary_frame()
print(pred_summary)  # includes mean, CI, prediction intervals

# Diagnostics
from statsmodels.stats.diagnostic import het_breuschpagan
bp_test = het_breuschpagan(results.resid, X)
print(f"Breusch-Pagan p-value: {bp_test[1]:.4f}")

# Visualize residuals
import matplotlib.pyplot as plt
plt.scatter(results.fittedvalues, results.resid)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.show()
```

### Logistic Regression (Binary Outcomes)

```python
from statsmodels.discrete.discrete_model import Logit

# Add constant
X = sm.add_constant(X_data)

# Fit logit model
model = Logit(y_binary, X)
results = model.fit()

print(results.summary())

# Odds ratios
odds_ratios = np.exp(results.params)
print("Odds ratios:\\n", odds_ratios)

# Predicted probabilities
probs = results.predict(X)

# Binary predictions (0.5 threshold)
predictions = (probs > 0.5).astype(int)

# Model evaluation
from sklearn.metrics import classification_report, roc_auc_score

print(classification_report(y_binary, predictions))
print(f"AUC: {roc_auc_score(y_binary, probs):.4f}")

# Marginal effects
marginal = results.get_margeff()
print(marginal.summary())
```

### Time Series (ARIMA)

```python
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Check stationarity
from statsmodels.tsa.stattools import adfuller

adf_result = adfuller(y_series)
print(f"ADF p-value: {adf_result[1]:.4f}")

if adf_result[1] > 0.05:
    # Series is non-stationary, difference it
    y_diff = y_series.diff().dropna()

# Plot ACF/PACF to identify p, q
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
plot_acf(y_diff, lags=40, ax=ax1)
plot_pacf(y_diff, lags=40, ax=ax2)
plt.show()

# Fit ARIMA(p,d,q)
model = ARIMA(y_series, order=(1, 1, 1))
results = model.fit()

print(results.summary())

# Forecast
forecast = results.forecast(steps=10)
forecast_obj = results.get_forecast(steps=10)
forecast_df = forecast_obj.summary_frame()

print(forecast_df)  # includes mean and confidence intervals

# Residual diagnostics
results.plot_diagnostics(figsize=(12, 8))
plt.show()
```

### Generalized Linear Models (GLM)

```python
import statsmodels.api as sm

# Poisson regression for count data
X = sm.add_constant(X_data)
model = sm.GLM(y_counts, X, family=sm.families.Poisson())
results = model.fit()

print(results.summary())

# Rate ratios (for Poisson with log link)
rate_ratios = np.exp(results.params)
print("Rate ratios:\\n", rate_ratios)

# Check overdispersion
overdispersion = results.pearson_chi2 / results.df_resid
print(f"Overdispersion: {overdispersion:.2f}")

if overdispersion > 1.5:
    # Use Negative Binomial instead
    from statsmodels.discrete.count_model import NegativeBinomial
    nb_model = NegativeBinomial(y_counts, X)
    nb_results = nb_model.fit()
    print(nb_results.summary())
```

## Core Statistical Modeling Capabilities

### 1. Linear Regression Models

Comprehensive suite of linear models for continuous outcomes with various error structures.

**Available models:**
- **OLS**: Standard linear regression with i.i.d. errors
- **WLS**: Weighted least squares for heteroskedastic errors
- **GLS**: Generalized least squares for arbitrary covariance structure
- **GLSAR**: GLS with autoregressive errors for time series
- **Quantile Regression**: Conditional quantiles (robust to outliers)
- **Mixed Effects**: Hierarchical/multilevel models with random effects
- **Recursive/Rolling**: Time-varying parameter estimation

**Key features:**
- Comprehensive diagnostic tests
- Robust standard errors (HC, HAC, cluster-robust)
- Influence statistics (Cook's distance, leverage, DFFITS)
- Hypothesis testing (F-tests, Wald tests)
- Model comparison (AIC, BIC, likelihood ratio tests)
- Prediction with confidence and prediction intervals

**When to use:** Continuous outcome variable, want inference on coefficients, need diagnostics

**Reference:** See `references/linear_models.md` for detailed guidance on model selection, diagnostics, and best practices.

### 2. Generalized Linear Models (GLM)

Flexible framework extending linear models to non-normal distributions.

**Distribution families:**
- **Binomial**: Binary outcomes or proportions (logistic regression)
- **Poisson**: Count data
- **Negative Binomial**: Overdispersed counts
- **Gamma**: Positive continuous, right-skewed data
- **Inverse Gaussian**: Positive continuous with specific variance structure
- **Gaussian**: Equivalent to OLS
- **Tweedie**: Flexible family for semi-continuous data

**Link functions:**
- Logit, Probit, Log, Identity, Inverse, Sqrt, CLogLog, Power
- Choose based on interpretation needs and model fit

**Key features:**
- Maximum likelihood estimation via IRLS
- Deviance and Pearson residuals
- Goodness-of-fit statistics
- Pseudo R-squared measures
- Robust standard errors

**When to use:** Non-normal outcomes, need flexible variance and link specifications

**Reference:** See `references/glm.md` for family selection, link functions, interpretation, and diagnostics.

### 3. Discrete Choice Models

Models for categorical and count outcomes.

**Binary models:**
- **Logit**: Logistic regression (odds ratios)
- **Probit**: Probit regression (normal distribution)

**Multinomial models:**
- **MNLogit**: Unordered categories (3+ levels)
- **Conditional Logit**: Choice models with alternative-specific variables
- **Ordered Model**: Ordinal outcomes (ordered categories)

**Count models:**
- **Poisson**: Standard count model
- **Negative Binomial**: Overdispersed counts
- **Zero-Inflated**: Excess zeros (ZIP, ZINB)
- **Hurdle Models**: Two-stage models for zero-heavy data

**Key features:**
- Maximum likelihood estimation
- Marginal effects at means or average marginal effects
- Model comparison via AIC/BIC
- Predicted probabilities and classification
- Goodness-of-fit tests

**When to use:** Binary, categorical, or count outcomes

**Reference:** See `references/discrete_choice.md` for model selection, interpretation, and evaluation.

### 4. Time Series Analysis

Comprehensive time series modeling and forecasting capabilities.

**Univariate models:**
- **AutoReg (AR)**: Autoregressive models
- **ARIMA**: Autoregressive integrated moving average
- **SARIMAX**: Seasonal ARIMA with exogenous variables
- **Exponential Smoothing**: Simple, Holt, Holt-Winters
- **ETS**: Innovations state space models

**Multivariate models:**
- **VAR**: Vector autoregression
- **VARMAX**: VAR with MA and exogenous variables
- **Dynamic Factor Models**: Extract common factors
- **VECM**: Vector error correction models (cointegration)

**Advanced models:**
- **State Space**: Kalman filtering, custom specifications
- **Regime Switching**: Markov switching models
- **ARDL**: Autoregressive distributed lag

**Key features:**
- ACF/PACF analysis for model identification
- Stationarity tests (ADF, KPSS)
- Forecasting with prediction intervals
- Residual diagnostics (Ljung-Box, heteroskedasticity)
- Granger causality testing
- Impulse response functions (IRF)
- Forecast error variance decomposition (FEVD)

**When to use:** Time-ordered data, forecasting, understanding temporal dynamics

**Reference:** See `references/time_series.md` for model selection, diagnostics, and forecasting methods.

### 5. Statistical Tests and Diagnostics

Extensive testing and diagnostic capabilities for model validation.

**Residual diagnostics:**
- Autocorrelation tests (Ljung-Box, Durbin-Watson, Breusch-Godfrey)
- Heteroskedasticity tests (Breusch-Pagan, White, ARCH)
- Normality tests (Jarque-Bera, Omnibus, Anderson-Darling, Lilliefors)
- Specification tests (RESET, Harvey-Collier)

**Influence and outliers:**
- Leverage (hat values)
- Cook's distance
- DFFITS and DFBETAs
- Studentized residuals
- Influence plots

**Hypothesis testing:**
- t-tests (one-sample, two-sample, paired)
- Proportion tests
- Chi-square tests
- Non-parametric tests (Mann-Whitney, Wilcoxon, Kruskal-Wallis)
- ANOVA (one-way, two-way, repeated measures)

**Multiple comparisons:**
- Tukey's HSD
- Bonferroni correction
- False Discovery Rate (FDR)

**Effect sizes and power:**
- Cohen's d, eta-squared
- Power analysis for t-tests, proportions
- Sample size calculations

**Robust inference:**
- Heteroskedasticity-consistent SEs (HC0-HC3)
- HAC standard errors (Newey-West)
- Cluster-robust standard errors

**When to use:** Validating assumptions, detecting problems, ensuring robust inference

**Reference:** See `references/stats_diagnostics.md` for comprehensive testing and diagnostic procedures.

## Formula API (R-style)

Statsmodels supports R-style formulas for intuitive model specification:

```python
import statsmodels.formula.api as smf

# OLS with formula
results = smf.ols('y ~ x1 + x2 + x1:x2', data=df).fit()

# Categorical variables (automatic dummy coding)
results = smf.ols('y ~ x1 + C(category)', data=df).fit()

# Interactions
results = smf.ols('y ~ x1 * x2', data=df).fit()  # x1 + x2 + x1:x2

# Polynomial terms
results = smf.ols('y ~ x + I(x**2)', data=df).fit()

# Logit
results = smf.logit('y ~ x1 + x2 + C(group)', data=df).fit()

# Poisson
results = smf.poisson('count ~ x1 + x2', data=df).fit()

# ARIMA (not available via formula, use regular API)
```

## Model Selection and Comparison

### Information Criteria

```python
# Compare models using AIC/BIC
models = {
    'Model 1': model1_results,
    'Model 2': model2_results,
    'Model 3': model3_results
}

comparison = pd.DataFrame({
    'AIC': {name: res.aic for name, res in models.items()},
    'BIC': {name: res.bic for name, res in models.items()},
    'Log-Likelihood': {name: res.llf for name, res in models.items()}
})

print(comparison.sort_values('AIC'))
# Lower AIC/BIC indicates better model
```

### Likelihood Ratio Test (Nested Models)

```python
# For nested models (one is subset of the other)
from scipy import stats

lr_stat = 2 * (full_model.llf - reduced_model.llf)
df = full_model.df_model - reduced_model.df_model
p_value = 1 - stats.chi2.cdf(lr_stat, df)

print(f"LR statistic: {lr_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Full model significantly better")
else:
    print("Reduced model preferred (parsimony)")
```

### Cross-Validation

```python
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = []

for train_idx, val_idx in kf.split(X):
    X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
    y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

    # Fit model
    model = sm.OLS(y_train, X_train).fit()

    # Predict
    y_pred = model.predict(X_val)

    # Score
    rmse = np.sqrt(mean_squared_error(y_val, y_pred))
    cv_scores.append(rmse)

print(f"CV RMSE: {np.mean(cv_scores):.4f} ± {np.std(cv_scores):.4f}")
```

## Best Practices

### Data Preparation

1. **Always add constant**: Use `sm.add_constant()` unless excluding intercept
2. **Check for missing values**: Handle or impute before fitting
3. **Scale if needed**: Improves convergence, interpretation (but not required for tree models)
4. **Encode categoricals**: Use formula API or manual dummy coding

### Model Building

1. **Start simple**: Begin with basic model, add complexity as needed
2. **Check assumptions**: Test residuals, heteroskedasticity, autocorrelation
3. **Use appropriate model**: Match model to outcome type (binary→Logit, count→Poisson)
4. **Consider alternatives**: If assumptions violated, use robust methods or different model

### Inference

1. **Report effect sizes**: Not just p-values
2. **Use robust SEs**: When heteroskedasticity or clustering present
3. **Multiple comparisons**: Correct when testing many hypotheses
4. **Confidence intervals**: Always report alongside point estimates

### Model Evaluation

1. **Check residuals**: Plot residuals vs fitted, Q-Q plot
2. **Influence diagnostics**: Identify and investigate influential observations
3. **Out-of-sample validation**: Test on holdout set or cross-validate
4. **Compare models**: Use AIC/BIC for non-nested, LR test for nested

### Reporting

1. **Comprehensive summary**: Use `.summary()` for detailed output
2. **Document decisions**: Note transformations, excluded observations
3. **Interpret carefully**: Account for link functions (e.g., exp(β) for log link)
4. **Visualize**: Plot predictions, confidence intervals, diagnostics

## Common Workflows

### Workflow 1: Linear Regression Analysis

1. Explore data (plots, descriptives)
2. Fit initial OLS model
3. Check residual diagnostics
4. Test for heteroskedasticity, autocorrelation
5. Check for multicollinearity (VIF)
6. Identify influential observations
7. Refit with robust SEs if needed
8. Interpret coefficients and inference
9. Validate on holdout or via CV

### Workflow 2: Binary Classification

1. Fit logistic regression (Logit)
2. Check for convergence issues
3. Interpret odds ratios
4. Calculate marginal effects
5. Evaluate classification performance (AUC, confusion matrix)
6. Check for influential observations
7. Compare with alternative models (Probit)
8. Validate predictions on test set

### Workflow 3: Count Data Analysis

1. Fit Poisson regression
2. Check for overdispersion
3. If overdispersed, fit Negative Binomial
4. Check for excess zeros (consider ZIP/ZINB)
5. Interpret rate ratios
6. Assess goodness of fit
7. Compare models via AIC
8. Validate predictions

### Workflow 4: Time Series Forecasting

1. Plot series, check for trend/seasonality
2. Test for stationarity (ADF, KPSS)
3. Difference if non-stationary
4. Identify p, q from ACF/PACF
5. Fit ARIMA or SARIMAX
6. Check residual diagnostics (Ljung-Box)
7. Generate forecasts with confidence intervals
8. Evaluate forecast accuracy on test set

## Reference Documentation

This skill includes comprehensive reference files for detailed guidance:

### references/linear_models.md
Detailed coverage of linear regression models including:
- OLS, WLS, GLS, GLSAR, Quantile Regression
- Mixed effects models
- Recursive and rolling regression
- Comprehensive diagnostics (heteroskedasticity, autocorrelation, multicollinearity)
- Influence statistics and outlier detection
- Robust standard errors (HC, HAC, cluster)
- Hypothesis testing and model comparison

### references/glm.md
Complete guide to generalized linear models:
- All distribution families (Binomial, Poisson, Gamma, etc.)
- Link functions and when to use each
- Model fitting and interpretation
- Pseudo R-squared and goodness of fit
- Diagnostics and residual analysis
- Applications (logistic, Poisson, Gamma regression)

### references/discrete_choice.md
Comprehensive guide to discrete outcome models:
- Binary models (Logit, Probit)
- Multinomial models (MNLogit, Conditional Logit)
- Count models (Poisson, Negative Binomial, Zero-Inflated, Hurdle)
- Ordinal models
- Marginal effects and interpretation
- Model diagnostics and comparison

### references/time_series.md
In-depth time series analysis guidance:
- Univariate models (AR, ARIMA, SARIMAX, Exponential Smoothing)
- Multivariate models (VAR, VARMAX, Dynamic Factor)
- State space models
- Stationarity testing and diagnostics
- Forecasting methods and evaluation
- Granger causality, IRF, FEVD

### references/stats_diagnostics.md
Comprehensive statistical testing and diagnostics:
- Residual diagnostics (autocorrelation, heteroskedasticity, normality)
- Influence and outlier detection
- Hypothesis tests (parametric and non-parametric)
- ANOVA and post-hoc tests
- Multiple comparisons correction
- Robust covariance matrices
- Power analysis and effect sizes

**When to reference:**
- Need detailed parameter explanations
- Choosing between similar models
- Troubleshooting convergence or diagnostic issues
- Understanding specific test statistics
- Looking for code examples for advanced features

**Search patterns:**
```bash
# Find information about specific models
grep -r "Quantile Regression" references/

# Find diagnostic tests
grep -r "Breusch-Pagan" references/stats_diagnostics.md

# Find time series guidance
grep -r "SARIMAX" references/time_series.md
```

## Common Pitfalls to Avoid

1. **Forgetting constant term**: Always use `sm.add_constant()` unless no intercept desired
2. **Ignoring assumptions**: Check residuals, heteroskedasticity, autocorrelation
3. **Wrong model for outcome type**: Binary→Logit/Probit, Count→Poisson/NB, not OLS
4. **Not checking convergence**: Look for optimization warnings
5. **Misinterpreting coefficients**: Remember link functions (log, logit, etc.)
6. **Using Poisson with overdispersion**: Check dispersion, use Negative Binomial if needed
7. **Not using robust SEs**: When heteroskedasticity or clustering present
8. **Overfitting**: Too many parameters relative to sample size
9. **Data leakage**: Fitting on test data or using future information
10. **Not validating predictions**: Always check out-of-sample performance
11. **Comparing non-nested models**: Use AIC/BIC, not LR test
12. **Ignoring influential observations**: Check Cook's distance and leverage
13. **Multiple testing**: Correct p-values when testing many hypotheses
14. **Not differencing time series**: Fit ARIMA on non-stationary data
15. **Confusing prediction vs confidence intervals**: Prediction intervals are wider

## Getting Help

For detailed documentation and examples:
- Official docs: https://www.statsmodels.org/stable/
- User guide: https://www.statsmodels.org/stable/user-guide.html
- Examples: https://www.statsmodels.org/stable/examples/index.html
- API reference: https://www.statsmodels.org/stable/api.html



<!-- MERGED INTO: data-science-python on 2026-04-18 -->
<!-- Use `data-science-python` instead. -->
