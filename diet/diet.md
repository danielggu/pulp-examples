# Diet Mix Problem

The aim of this problem is to determine the optimal food mix which minimizes the total cost and ensures a certain minimum nutrient intake.

## Problem statement

Jimmy is a rancher. He has to feed their cows in order to ensure certain minimum nutrients intake; this requirements are 700g of protein, 28g of calcium and 150mg of vitamins. To get this purpose, he has two different foods available (*a*, *b*), each of them has a known nutrient distribution per kilogram which is included in the following table.

|       | Protein(g) | Calcium(g) | Vitamin(mg) |
| ----- | :--------: | :--------: |:-----------:|
|  *a*  |      30    |      2     |      10     |
|  *b*  |      45    |      1     |      5      |

Jimmy could feed their cows using only one of this this two foods, or maybe a mix of both. However, they have different prices (0.3 $/kg for product *a* and 0.35 $/kg for product *b*), so Jimmy wonders what is the optimal mix which minimizes the cost of feeding their cows.

Can we help Jimmy?

## Mathematical formulation

Here is summarized the formulation of the diet mix problem. Python code solution follows the same nomenclature in order to facilitate its comprehension and clarity.

### Nomenclature

| Indexes | Description|
| :---: | :-: | :-: |
|  *i*  | foods |
|  *j*  | nutrients |
&nbsp;

| Parameters | Description|
| :---: | :-: | :-: |
|  $p_{ij}$ | quantity of nutrient *j* per kilogram of food *i* |
|  $q_j$ | minimum requirements of nutrient *j* |
|  $c_i$ | cost per kilogram of food *i* |
&nbsp;

| Variables | Description|
| :---: | :-: | :-: |
|  $x_i$ | optimal quantity of food *i* |

### Equations

#### Objective function
$$min \sum_i c_i x_i$$
#### Constraints
$$\sum_i p_{ij} x_i \geq b_j\ \forall j$$
$$x_i \geq 0\ \forall i$$
