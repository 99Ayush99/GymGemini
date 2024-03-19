from langchain_google_genai import GoogleGenerativeAI
import os
from langchain.prompts import PromptTemplate
import streamlit as st

st.set_page_config(page_title="GemFood", page_icon="https://emojicdn.elk.sh/💪🏻")
st.title("GemFood")
os.environ["GOOGLE_API_KEY"] = "AIzaSyA0UwntqzhSVO6djewuTgcb8lyWBQiLahg"

llm = GoogleGenerativeAI(model="gemini-pro",temperature=0)

option = st.sidebar.selectbox(
    'Select the task:',
    ('General Queries','Nutrition','Recipe','Meal Recommendations')
)

if option=='Nutrition':
    def get_nutrition(food,measurements):
        template = """
        You have a very good knowledge in food nutritional facts. You will be provided food items and their measurements, you have to print all the nutritional facts of the food items as per the measurements.
        Food Item: {food}
        Measurement: {measurements}
        """

        prompt = PromptTemplate.from_template(template)
        chain = prompt | llm

        return chain.invoke({"food":food,"measurements":measurements})

    food = st.text_input(label="Enter the food item")
    measurements = st.text_input(label="Enter the measurement of the food item")
    if food and measurements:
        st.write(get_nutrition(food,measurements))
elif option=='Recipe':
    def get_recipe(food,people):
        template = """
        You are a healthy chef and can provide very accurate healthy recipes for any food item. You will be provided a food item and the number of people that food is to be served. You have to provide the whole recipe with quantity and necessary steps to prepare that food.Give the calories too of ingredients used according to the quantity and final calory of the dish. Weight in grams
        Food: {food}
        Number of People: {people}
        """

        prompt = PromptTemplate.from_template(template)
        chain = prompt | llm
        if food and people:
            return chain.invoke({"food":food,"people":people})
    
    food = st.text_input(label="Enter the food item")
    people = st.text_input(label="Enter the number of people")

    st.write(get_recipe(food,people))
elif option=='Meal Recommendations':
    def get_meal_recommendation(goal):
        template = """
        You are a nutritionist and can suggest 5 meal plan(Breakfast,Snacks,Lunch,Snacks,Dinner) according to the fitness goal of the user. Give the food items along with quantity and calories.
        At the end print the whole plan Macro Nutrients
        Goal:{goal}
        """

        prompt = PromptTemplate.from_template(template)
        chain = prompt | llm

        return chain.invoke({"goal":goal})
    
    goal = st.text_input(label="Enter your fitness goal")
    if goal:
        st.write(get_meal_recommendation(goal))
elif option=='General Queries':
    def solve_query(query):
        template="""
        You are a nutritionaist and can solve queries about foods with expertise.You have to use that expertise to solve the given query.
        Query: {query}
        """

        prompt = PromptTemplate.from_template(template)
        chain = prompt | llm

        return chain.invoke({'query':query})
    
    query = st.text_input(label="Enter your Query")
    if query:
        st.write(solve_query(query))