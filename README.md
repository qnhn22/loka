**Project:** Loka.ai/**Members:** Quan Nguyen, Duc Nguyen, Long Bui

## I. Motivations
While small businesses represent 44% of the U.S. GDP, 99% of all firms, and have generated 63% of new jobs over the last decade, they face challenges in leveraging data-driven decision-making to enhance profitability comparing larger enterprises. This may be due to the lack of resources and experience necessary to implement data-driven technologies and invest in research and development. 

A platform that could help small firms to **optimize** their **financial resosurces** and **understand** of **market dynamics** has become more **urgent**.

## II. Solution Overview
Given our limited resources and time, we aim to focus on a specific area that best showcases the potential of this approach:

_An innovative approach to identify the **ideal locations** for small-scale food and beverage enterprises._

Most optimized location. **What it demonstrates ?**

- Customer demographics
- Potential Markets
- Rental & operational costs
- Competitor presence


Focusing first on F&B industry. **Why F&B ?**
- **99.9%** of businesses in F&B industry are small firms.
- **56%** of F&B business owners struggle with managing operational costs and profitability
- **52%** cite economic uncertainty as a major hurdleeconomic uncertainty as a significant hurdle.
- The U.S. packaged food market is projected to reach **US$1.6 trillion** by 2030

## III. Milestones & Challenges

![System Diagram](https://raw.githubusercontent.com/qnhn22/loka/refs/heads/main/pics/system_diagram.png)


- Pull APIs from different data sources (GoogleMapAPI, Census Bureau, NY Open Data)
- Integrate pulled data into [MongoDB](https://github.com/mongodb/mongo)
- Utilize [React](https://github.com/facebook/react) to construct web interface
- Optimize [Flask](https://github.com/pallets/flask) to build server
- Develop a machine learning model that captures essential parameters using [Cerebas API](https://github.com/Cerebras) to rank most optimized locations
- Leverage [PropelAuthority](https://github.com/orgs/PropelAuth/repositories) to authorize user management
- Design, reorganize, and visualize metrics into meaningful and understandable insights


## IV. Takeaways
### Pros

+ **Operational and Functional**: The app is fully operational, allowing users to access its features seamlessly, enabling immediate utilization for business enhancement.

+ **Showcases Essential Capabilities**: It effectively demonstrates the necessary skills and functionalities, providing valuable insights for optimizing processes and decision-making. 

+ **Room for Improvements**: The project shows solid foundation that could potentially develop new features and continous improvability in the future. 

### Cons

+ **Potential Model Biases**: Some biases have been identified in the model, which may affect accuracy. Further testing and fine-tuning are needed to improve reliability.

+ **Capacity Limitations**: The app currently has restrictions on handling larger datasets and accommodating more users, necessitating enhancements for scalability.

+ **Data Dependencies**: Fetching data from different sources and does not have inernal data may lead to disrupt the system if sources collasped.

## V. Future Enhancements
### Model Improvements:
1. **Market Equilibrium Adjustment**: 
Implement dynamic Supply & Demand balancing algorithms to reflect real-time market conditions.
2. **Logistics Analysis Implementation**: Incorporate advanced logistics modeling to optimize supply chain operations and reduce costs.
3. **Data Backup Sources**: Utilize redundant cloud storage, regular snapshots, and blockchain technology for secure and reliable data backups.
4. **Features Added**: Introduce machine learning price predictions, real-time sentiment analysis, customizable alerts, and interactive visualizations.

### Platform Integrations:
1. **Market Data Providers:** Establish connections with providers like Bloomberg for comprehensive market data feeds.
2. **Integration with CRM Systems**: Connect with platforms like Microsoft Business Central (launched in 2021 to serve small business's data solutions) to retreive more accurate financial data.
