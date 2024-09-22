import re
from models.rank_abc import RankInterface
import os
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv
import numpy as np
load_dotenv()


class CerebrasOp(RankInterface):
    def __init__(self, data):
        super().__init__(data)
        self.client = Cerebras(
            api_key=os.environ.get("CEREBRAS_API"),
        )

    def rank_data(self):
        query = "Here are data " + \
            np.array2string(
                self.data)+", aim is to maximize the first, minimize the second, maximize the third, remember to normalize, rearrange the data in form of np array with ranking high to low, only number please"
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": query
                }
            ],
            model="llama3.1-8b",
        )
        response = chat_completion.choices[0].message.content
        print(response)
        array_str = re.search(r"np\.array\(([\s\S]*?)\)", response).group(1)
        data = np.array(eval(array_str))
        return data


if __name__ == "__main__":
    np.random.seed(42)
    n_points = 10
    distance = np.random.uniform(50, 300, n_points)
    price = np.random.uniform(100, 1000, n_points)
    population = np.random.uniform(10000, 100000, n_points)
    data = np.column_stack((distance, price, population))
    cerebras_opt = CerebrasOp(data)
    cerebras_front = cerebras_opt.rank_data()
