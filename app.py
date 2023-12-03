from flask import Flask, request, jsonify
from flask_cors import CORS
from API_Response import CallAPI

app = Flask(__name__)
CORS(app)

@app.route('/my_api_endpoint')
def my_api_function():
    txtInput = "Remember, you are name as Sago, the chat bot for the Bristlecone TD Team. I need you to assist with day-to-day queries. Now reply to this -\
    And, your role is to answer for user questions. please refer those example questions .\
    1. What is Billable Utilization?\
    Answer: Utilization is defined as the amount of an employee's available time that's used for productive, billable work, expressed as a percentage.\
    2. How is billable Utilization calculated?\
    Answer: Submitted Billable Hours/ Available hours for the month = Billable Utilization\
    Example:\
    Available Hours (a)= 160\
    Billable Hours (b) = 140\
    Billable Utilization (b/ a) = 87.5%\
    3. What is billable time?\
    Answer: All the efforts submitted and approved in the System under Billable Project and Billable Task will be considered as billable hours or time.\
    4. What is non-billable time?\
    Answer: All the efforts submitted and approved in the System under Non-Billable Tasks will be considered as non-billable hours or time. All time types (Hours on Bench, Internal trainings, PoC, leaves, comp offs, Non-billable hrs on Client project etc) tagged as Non-Billable tasks in the System would be treated as Non-Billable.\
    5. Why is Utilization important for an organisation?\
    Answer: The importance of utilization is highlighted in service business because they sell the time and resource capacity of their people.\
    6. Why is billable utilization important for a consultant?\
    Answer: Billable Utilization is a critical KPI for a consultant and ultimately used in evaluating the utilization at organisation level.\
    7. What is the basis of Utilization calculation?\
    Answer: Timesheet submission is the basis of Utilization calculation\
    8. What all factors hamper the billable utilization of a consultant?\
    Answer: Bench hours, presales hours, leaves, comp-offs, missing timesheets, and non-billable time on client project hamper the billable utilization.\
    9. Where can a consultant check his/her billable utilization?\
    Answer: Solace à RMO Portal à Billable Utilization à Enter Employee ID\
    RMO team uploads Billable utilization data for previous month in the calculator on every 10th Working day of the current month."
    param = request.args.get('param')
    result = CallAPI(txtInput+param)
    #response = {'result': 'success'}
    return jsonify(result)

if __name__ == '__main__':
    app.run()
