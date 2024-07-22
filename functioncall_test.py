from openai import OpenAI
import json

client = OpenAI(api_key='sk-proj-YQsnoQpfIfRAgayFSFpyT3BlbkFJBrzUahRSpYru1nlOopnd')

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": unit})
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})

def run_conversation():
    # Step 1: send the conversation and available functions to the model
    messages = [{"role": "user", "content": "What's the weather like in San Francisco, Tokyo, and Paris?"}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response_message = response.choices[0].message

    tool_calls = response_message.tool_calls        #获取可以调用的方法
    # Step 2: check if the model wanted to call a function 检测模型是否愿意调用函数
    if tool_calls:

        # Step 3: call the function 调用函数
        # Note: the JSON response may not always be valid; be sure to handle errors 
        #建立函数键值对映射
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # only one function in this example, but you can have multiple

        messages.append(response_message)  #extend conversation with assistant's reply

        # Step 4: send the info for each function call and function response to the model   
        for tool_call in tool_calls:
            function_name = tool_call.function.name                     #LLM愿意调用的函数方法
            function_to_call = available_functions[function_name]       #调用本地函数获得输出
            function_args = json.loads(tool_call.function.arguments)    #参数使用LLM返回的
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            messages.append(                                            #将函数信息传回LLM
                {
                    "tool_call_id": tool_call.id,                       #调用了什么函数
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,                       #本地函数返回了什么
                }
            )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        return second_response                                          #重新获取LLM输出
print(run_conversation())