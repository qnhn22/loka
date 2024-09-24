**Project:** Loka.ai

**Members:** Quan Nguyen, Duc Nguyen, Long Bui

## I. Motivations
An innovative platform to identify **ideal locations** for food & beverage enterprises, focusing on customer demographics, potential markets, costs, and competition. This approach addresses the needs of the F&B industry, where 97% are firms facing operational and economic challenges. With the U.S. packaged food market projected to reach $1.6 trillion by 2030, optimizing location decisions is crucial for success

## II. Milestones & Challenges

![System Diagram](https://raw.githubusercontent.com/qnhn22/loka/refs/heads/main/pics/system_diagram.png)


- Aggregate data by leveraging APIs from multiple sources" (GoogleMapAPI, Census Bureau, NY Open Data)
- Integrate and clean pulled data into [MongoDB](https://github.com/mongodb/mongo)
- Develop a responsive web interface using [React](https://github.com/facebook/react)
- Enhance server-side performance by implementing [Flask](https://github.com/pallets/flask)
- Develop a machine learning model that captures essential parameters using [Cerebas API](https://github.com/Cerebras) to rank most optimized locations
- Leverage [PropelAuthority](https://github.com/orgs/PropelAuth/repositories) to authorize user management
- Design, reorganize, and visualize metrics into meaningful and understandable insights


## III. Takeaways
### Pros

+ **Operational and Functional**: The app is fully operational, allowing users to access its features seamlessly, enabling immediate utilization for business enhancement.

+ **Showcases Essential Capabilities**: It effectively demonstrates the necessary skills and functionalities, providing valuable insights for optimizing processes and decision-making. 

+ **Room for Improvements**: The project shows solid foundation that could potentially develop new features and continous improvability in the future. 

### Cons

+ **Potential Model Biases**: Some biases have been identified in the model, which may affect accuracy. Further testing and fine-tuning are needed to improve reliability.

+ **Capacity Limitations**: The app currently has restrictions on handling larger datasets and accommodating more users, necessitating enhancements for scalability.

+ **Data Dependencies**: Fetching data from different sources and does not have inernal data may lead to disrupt the system if sources collasped.

## IV. Future Enhancements
### Model Improvements:
1. **Market Equilibrium Adjustment**: 
Implement dynamic Supply & Demand balancing algorithms to reflect real-time market conditions.
2. **Logistics Analysis Implementation**: Incorporate advanced logistics modeling to optimize supply chain operations and reduce costs.
3. **Data Backup Sources**: Utilize redundant cloud storage, regular snapshots, and blockchain technology for secure and reliable data backups.
4. **Features Added**: Introduce machine learning price predictions, real-time sentiment analysis, customizable alerts, and interactive visualizations.

### Platform Integrations:
1. **Market Data Providers:** Establish connections with providers like Bloomberg for comprehensive market data feeds.
2. **Integration with CRM Systems**: Connect with platforms like Microsoft Business Central (launched in 2021 to serve small business's data solutions) to retreive more accurate financial data.
