# -*- coding: utf-8 -*-
"""log_analyzer.ipynb

# Programming Assignment 2, CSE30-02, Winter 2023

## README

* Please follow the instructions given below (in the comments) to 
  use this Colab notebook
  * Only edit within the allowed sections as instructed by the
    comments
  * DO NOT change anything outside those sections
* Testing script is provided at the end to help you to ensure your 
  implementation is compatible with the autograder
  * If your code doesn't work with the testing script, it's not 
    compatible with the autograder; so it will fail the grading 
    for sure
  * If your code work with the testing script, it's compatible 
    with the autograder; but, this **DOES NOT** guarantee your 
    output will be correct for the inputs we provided during the 
    grading process
* To run the testing script, on menu bar, click `Runtime` -> `Run all`
* After you finished testing your code, you may download this notebook
  containing your code as **.py** file, and submit to Canvas
  * To download this notebook as .py file, on menu bar, 
    click `File` -> `Download` -> `Download .py`
"""

#===== You may add import statements below this line ----->

# Author: Vishruth Bharath
# Class: CSE30 W2023

import json
import pandas
import re
import numpy as np
from dateutil.parser import parse
from typing import List

#===== <----- Please keep import statements above this line

from pandas.core.computation.ops import Timestamp
def log_to_dataframe(
    src_log_filepath: str,
) -> pandas.DataFrame:
    '''
    - Parameters:
        - src_log_filepath: path to the log file
    - Returns:
        - pandas.DataFrame: a pandas.DataFrame object parsed from
          the log file
    '''
    #===== Please enter your implementation below this line ----->
    data_pattern = "(?P<host>.*?) .*? .*? \[(?P<timestamp>.*?)\] \"(?P<method>.*?) (?P<url>.*?) (?P<version>HTTP/.*)?\" (?P<response_code>\d*) (?P<content_size>\d*)"
    columns = ("host", "timestamp", "method", "url", "version", "response_code"
    , "content_size")

    data = {column:[] for column in columns}
    
    # 
    with open(src_log_filepath) as file:
        for line in file.readlines():
            regex_match = re.search(data_pattern, line)
            group_dict = regex_match.groupdict()

            for column in columns:
              val = group_dict[column]
              if column == "response_code" or column == "content_size":
                if val == "":
                  val = 0
                data[column].append(int(val))
              else:
                data[column].append(val)
           
                
    return pandas.DataFrame(data)

    #===== <----- Please keep your implementation above this line
    pass

def get_num_of_distinct_resp_code(data: pandas.DataFrame) -> int:
    '''
    - Parameters:
        - data: input dataframe, received from log_to_dataframe function call
    - Returns:
        - int: number of distinct response code
    '''
    #===== Please enter your implementation below this line ----->
    return len(pandas.unique(data.response_code))
    #===== <----- Please keep your implementation above this line
    pass


def get_median_content_size(data: pandas.DataFrame) -> int:
    '''
    - Parameters:
        - data: input dataframe, received from log_to_dataframe function call
    - Returns:
        - int: median content size
          - float numbers should be **type-casted** into integer numbers
    '''
    #===== Please enter your implementation below this line ----->
    content_size = np.array(data.content_size)
    return int(np.median(content_size[content_size != 0]))
    #===== <----- Please keep your implementation above this line
    pass

def get_most_freq_hosts(data: pandas.DataFrame, numOfHosts: int) -> List[str]:
    '''
    - Parameters:
        - data: input dataframe, received from log_to_dataframe function call
        - numOfHosts: top `numOfHosts` most frequency hosts
    - Returns:
        - List[str]: list of strings containing top `numOfHosts` most
          frequency hosts; ordered from top 1 to top `numOfHosts`
    '''
    #===== Please enter your implementation below this line ----->
    values = np.unique(data.host)
    return list(values[0:numOfHosts])
    #===== <----- Please keep your implementation above this line
    pass

def get_most_freq_urls(data: pandas.DataFrame, numOfUrls: int) -> List[str]:
    '''
    - Parameters:
        - data: input dataframe, received from log_to_dataframe function call
        - numOfUrls: top `numOfUrls` most frequency URLs
    - Returns:
        - List[str]: list of strings containing top `numOfUrls` 
          most frequency URLs; ordered from top 1 to top 
          `numOfUrls`
    '''
    #===== Please enter your implementation below this line ----->
    values = np.unique(data.url)
    return list(values[0:numOfUrls])
    #===== <----- Please keep your implementation above this line
    pass


def get_top_urls_recv_err(data: pandas.DataFrame, numOfUrls: int) -> List[str]:
    '''
    - Parameters:
        - data: input dataframe, received from log_to_dataframe function call
        - numOfUrls: top `numOfUrls` URLs that received error 
          response codes
    - Returns:
        - List[str]: list of strings containing top `numOfUrls`
          URLs that received error response codes; ordered from
          top 1 to top `numOfUrls`
    '''
    #===== Please enter your implementation below this line ----->
    urls = []
    top_urls = []
    for index,url in enumerate(data.url):
      response_code = data.response_code[index]
      if response_code != 200:
        urls.append(url)
    values = np.unique(urls)
    for i in range(0,numOfUrls):
      top_urls.append(str(values[i]))
    return top_urls
    #===== <----- Please keep your implementation above this line
    pass

def get_num_of_req_recv_404(data: pandas.DataFrame) -> int:
    '''
    - Parameters:
        - data: input dataframe, received from log_to_dataframe function call
    - Returns:
        - int: number of requests received 404 responses
    '''
    #===== Please enter your implementation below this line ----->
    count = 0
    for index,url in enumerate(data.url):
      response_code = data.response_code[index]
      if response_code == 404:
        count += 1
    return count
    #===== <----- Please keep your implementation above this line
    pass

def get_num_of_unique_hosts_daily(data: pandas.DataFrame) -> List[int]:
    '''
    - Parameters:
        - data: input dataframe, received from log_to_dataframe function call
    - Returns:
        - List[int]: List of integers of unique hosts on each 
          day, ordered from the earliest to latest date
    '''
    #===== Please enter your implementation below this line ----->
    def sortFunc(day):
      return day[0]
    days = {}
    sorted_days = []
    for index,host in enumerate(data.host):
      timestamp = data.timestamp[index]
      timestamp = parse(timestamp[:11])
      if timestamp in days and not host in days[timestamp]:
        days[timestamp].append(host)
      elif not timestamp in days:
        days[timestamp] = [host]
    for day in days:
      sorted_days.append(len(days[day]))
    return sorted_days
    #===== <----- Please keep your implementation above this line
    pass

def get_avg_num_of_req_per_host_daily(data: pandas.DataFrame) -> List[int]:
    '''
    - Parameters:
        - data: input dataframe, received from log_to_dataframe function call
    - Returns:
        - List[int]: List of integers of average requests per 
          host on each day, ordered from the earliest to 
          latest date
          - float numbers should be **type-casted** into integer numbers
    '''
    #===== Please enter your implementation below this line ----->
    days = {}
    sorted_days = []
    for index,host in enumerate(data.host):
      timestamp = data.timestamp[index]
      timestamp = parse(timestamp[:11])
      if not timestamp in days:
        days[timestamp] = []
      days[timestamp].append(host)
    for key, requests in days.items():
      values, count = np.unique(requests, return_counts=True)
      avg = np.average(count)
      days[key] = int(avg)
    for day in days:
      sorted_days.append(days[day])
    return sorted_days
    #===== <----- Please keep your implementation above this line
    pass

def write_results_to_json(
    res1: int,
    res2: int,
    res3: List[str],
    res4: List[str],
    res5: List[str],
    res6: int,
    res7: List[int],
    res8: List[int],
    dest_json_path: str
) -> None:
    '''
    - Parameters:
        - res1: result generated by the function corresponding to question 1
        - res2: result generated by the function corresponding to question 2
        - res3: result generated by the function corresponding to question 3
        - res4: result generated by the function corresponding to question 4
        - res5: result generated by the function corresponding to question 5
        - res6: result generated by the function corresponding to question 6
        - res7: result generated by the function corresponding to question 7
        - res8: result generated by the function corresponding to question 8
        - dest_json_path: filepath to write the json file to
    '''
    #===== Please enter your implementation below this line ----->
    result = {
      "get_num_of_distinct_resp_code": res1,
      "get_median_content_size": res2,
      "get_most_freq_hosts": res3,
      "get_most_freq_urls": res4,
      "get_top_urls_recv_err": res5,
      "get_num_of_req_recv_404": res6,
      "get_num_of_unique_hosts_daily": res7,
      "get_avg_num_of_req_per_host_daily": res8
      }
    with open(dest_json_path, 'w') as f:
      json.dump(result, f, indent = 4)
    #===== <----- Please keep your implementation above this line
    pass

LOG_FILE_PATH = 'test_input.log'
JSON_FILE_PATH = 'dest_json_path.json'

#XXXXX DO NOT change anything below this line ----->

def assert_ret_val(res: bool, funcName: str, hint: str) -> None:
    if not res:
        print('AssertionError: {} failed; {}'.format(funcName, hint))
        return False
    print('AssertionOK: {}'.format(funcName))
    return True

def main() -> None:

    # NOTE: here we only test the input/output date types
    # to ensure your code is compatible with autograder
    # During grading process, we will be inspecting the
    # actual content of the return values

    df = log_to_dataframe(LOG_FILE_PATH)
    print('DataFrame:\n', df)
    assert_ret_val(type(df) == pandas.DataFrame, 'log_to_dataframe', 'return type is wrong')

    res1 = get_num_of_distinct_resp_code(df)
    print('get_num_of_distinct_resp_code:', res1)
    assert_ret_val(type(res1) == int, 'get_num_of_distinct_resp_code', 'return type is wrong')

    res2 = get_median_content_size(df)
    print('get_median_content_size:', res2)
    assert_ret_val(type(res2) == int, 'get_median_content_size', 'return type is wrong')

    res3 = get_most_freq_hosts(df, 10)
    print('get_most_freq_hosts:', res3)
    if assert_ret_val(type(res3) == list, 'get_most_freq_hosts', 'return type is wrong'):
        for item in res3:
            assert_ret_val(type(item) == str, 'get_most_freq_hosts', 'return type is wrong')

    res4 = get_most_freq_urls(df, 10)
    print('get_most_freq_urls:', res4)
    if assert_ret_val(type(res4) == list, 'get_most_freq_urls', 'return type is wrong'):
        for item in res4:
            assert_ret_val(type(item) == str, 'get_most_freq_urls', 'return type is wrong')

    res5 = get_top_urls_recv_err(df, 10)
    print('get_top_urls_recv_err:', res5)
    if assert_ret_val(type(res5) == list, 'get_top_urls_recv_err', 'return type is wrong'):
        for item in res5:
            assert_ret_val(type(item) == str, 'get_top_urls_recv_err', 'return type is wrong')

    res6 = get_num_of_req_recv_404(df)
    print('get_num_of_req_recv_404:', res6)
    assert_ret_val(type(res6) == int, 'get_num_of_req_recv_404', 'return type is wrong')

    res7 = get_num_of_unique_hosts_daily(df)
    print('get_num_of_unique_hosts_daily:', res7)
    if assert_ret_val(type(res7) == list, 'get_num_of_unique_hosts_daily', 'return type is wrong'):
        for item in res7:
            assert_ret_val(type(item) == int, 'get_num_of_unique_hosts_daily', 'return type is wrong')

    res8 = get_avg_num_of_req_per_host_daily(df)
    print('get_avg_num_of_req_per_host_daily:', res8)
    if assert_ret_val(type(res8) == list, 'get_avg_num_of_req_per_host_daily', 'return type is wrong'):
        for item in res8:
            assert_ret_val(type(item) == int, 'get_avg_num_of_req_per_host_daily', 'return type is wrong')

    write_results_to_json(
        res1,
        res2,
        res3,
        res4,
        res5,
        res6,
        res7,
        res8,
        JSON_FILE_PATH
    )

    try:
        with open(JSON_FILE_PATH, 'r') as f:
            file_content = f.read()
            print('write_results_to_json:', file_content)
            res_c = json.loads(file_content)
            print('write_results_to_json:', res_c)
            assert_ret_val(type(res_c) == dict, 'write_results_to_json', 'json data type is wrong')
    except FileNotFoundError:
        assert_ret_val(False, 'write_results_to_json', 'json file is not found')
    except json.JSONDecodeError:
        assert_ret_val(False, 'write_results_to_json', 'json file content is invalid')

    print('Test finished')


if __name__ == '__main__':
    main()
#XXXXX <----- DO NOT change anything above this line
