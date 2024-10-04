# CSC4160 Assignment-1: EC2 Measurement (2 questions)

### Deadline: 23:59, Sep 22, Sunday
---

### Name:
### Student Id:
---

## Question 1: Measure the EC2 CPU and Memory performance

1. (1 mark) Report the name of measurement tool used in your measurements (you are free to choose any open source measurement software as long as it can measure CPU and memory performance). Please describe your configuration of the measurement tool, and explain why you set such a value for each parameter. Explain what the values obtained from measurement results represent (e.g., the value of your measurement result can be the execution time for a scientific computing task, a score given by the measurement tools or something else).

    > Your answer goes here.

2. (1 mark) Run your measurement tool on general purpose `t3.medium`, `m5.large`, and `c5d.large` Linux instances, respectively, and find the performance differences among them. Launch all instances in the **US East (N. Virginia)** region. What about the differences among these instances in terms of CPU and memory performance? Please try explaining the differences. 

    In order to answer this question, you need to complete the following table by filling out blanks with the measurement results corresponding to each instance type.

    | Size      | CPU performance | Memory performance |
    |-----------|-----------------|--------------------|
    | `t3.medium` |                 |                    |
    | `m5.large`  |                 |                    |
    | `c5d.large` |                 |                    |

    > Region: US East (N. Virginia)

## Question 2: Measure the EC2 Network performance

1. (1 mark) The metrics of network performance include **TCP bandwidth** and **round-trip time (RTT)**. Within the same region, what network performance is experienced between instances of the same type and different types? In order to answer this question, you need to complete the following table.  

    | Type          | TCP b/w (Mbps) | RTT (ms) |
    |---------------|----------------|----------|
    | `t3.medium`-`t3.medium` |                |          |
    | `m5.large`-`m5.large`  |                |          |
    | `c5n.large`-`c5n.large` |                |          |
    | `t3.medium`-`c5n.large`   |                |          |
    | `m5.large`-`c5n.large`  |                |          |
    | `m5.large`-`t3.medium` |                |          |

    > Region: US East (N. Virginia)

2. (1 mark) What about the network performance for instances deployed in different regions? In order to answer this question, you need to complete the following table.

    | Connection | TCP b/w (Mbps)  | RTT (ms) |
    |------------|-----------------|--------------------|
    | N. Virginia-Oregon |                 |                    |
    | N. Virginia-N. Virginia  |                 |                    |
    | Oregon-Oregon |                 |                    |

    > All instances are `c5.large`.

