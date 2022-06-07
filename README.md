# findmyjob

This is a simple web-service to find your job.

---

1. You can clone this repo and run code.

```
# clone this repo
git clone git@github.com:JKeun/findmyjob.git

# change dir
cd findmyjob/flask_api/

# run server.py
python server.py
```

2. After run `server.py`, You can open the web page in local: http://127.0.0.1:8080

![Screen Shot 2022-06-07 at 5 02 56 PM](https://user-images.githubusercontent.com/17041998/172328567-f592f31c-e6d4-47be-9e3b-2e681b4c6e33.png)

3. Please write what you want to do or what you're interested in and please click the button `Find my Job!`


---
This is an example.

Input 1
```
I like Python. my major is statistic.
I'm interested in finance and healthcare.
```

Result 1
```
Top 10 Recommended Job List

1. Research Analyst

2. Data Scientist

3. Java Developer

4. Data Analyst

5. Solution Architect

6. Director Of Engineering

7. Automation Engineer

8. Web Developer

9. QA Tester

10. Business Analyst
````

---
**Note that: DO NOT TRUST THE RESULTS 100% 😜**  
This model is very very biased. It because the train data is mainly a collection of JD in the technical field.
