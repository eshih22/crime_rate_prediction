from flask import Flask, request, jsonify,render_template
import joblib

app = Flask(__name__)
random_regressor = joblib.load('random_forest_regressor.pkl')  # Load your trained Random Forest model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form  # Get form data
    features = [
        float(data.get('less_than_9th_grade', 0)),
        float(data.get('percent_less_than_9th_grade', 0)),
        float(data.get('ninth_to_twelfth', 0)),
        float(data.get('percent_ninth_to_twelfth', 0)),
        float(data.get('highschool_grad', 0)),
        float(data.get('percent_highschool_grad', 0)),
        float(data.get('some_college_no_degree', 0)),
        float(data.get('percent_some_college_no_degree', 0)),
        float(data.get('associates_degree', 0)),
        float(data.get('percent_associates_degree', 0)),
        float(data.get('bachelors_degree', 0)),
        float(data.get('percent_bachelors_degree', 0)),
        float(data.get('graduate_degree', 0)),
        float(data.get('percent_graduate_degree', 0)),
        float(data.get('Total_population', 0)),
        float(data.get('under_five', 0)),
        float(data.get('percent_under_five', 0)),
        float(data.get('five_to_nine', 0)),
        float(data.get('percent_five_to_nine', 0)),
        float(data.get('ten_to_fourteen', 0)),
        float(data.get('percent_ten_to_fourteen', 0)),
        float(data.get('fifteen_to_nineteen', 0)),
        float(data.get('percent_fifteen_to_nineteen', 0)),
        float(data.get('twenty_to_twentyfour', 0)),
        float(data.get('percent_twenty_to_twentyfour', 0)),
        float(data.get('twentyfive_to_thirtyfour', 0)),
        float(data.get('percent_twentyfive_to_thirtyfour', 0)),
        float(data.get('thirtyfive_to_fourtyfour', 0)),
        float(data.get('percent_thirtyfive_to_fourtyfour', 0)),
        float(data.get('fourtyfive_to_fiftyfour', 0)),
        float(data.get('percent_fourtyfive_to_fiftyfour', 0)),
        float(data.get('fiftyfive_to_fiftynine', 0)),
        float(data.get('percent_fiftyfive_to_fiftynine', 0)),
        float(data.get('sixty_to_sixtyfour', 0)),
        float(data.get('percent_sixty_to_sixtyfour', 0)),
        float(data.get('sixtyfive_to_seventyfour', 0)),
        float(data.get('percent_sixtyfive_to_seventyfour', 0)),
        float(data.get('seventyfive_to_eightyfour', 0)),
        float(data.get('percent_seventyfive_to_eightyfour', 0)),
        float(data.get('over_eightyfive', 0)),
        float(data.get('percent_over_eightyfive', 0)),
        float(data.get('unemployment_rate', 0)),
        float(data.get('income', 0)),
        float(data.get('house_price', 0)),
        float(data.get('percent_poverty', 0)),
        float(data.get('total_homes', 0)),
        float(data.get('owner_occupied', 0)),
        float(data.get('renter_occupied', 0)),
        float(data.get('percent_owner_occupied', 0)),
        float(data.get('percent_renter_occupied', 0)),
        float(data.get('percent_over_twentyfive', 0)),
        float(data.get('percent_under_fourteen', 0)),
        float(data.get('percent_young_adults', 0)),
        float(data.get('percent_uneducated', 0)),
        float(data.get('percent_higher_education', 0)),
        float(data.get('total_uneducated', 0)),
        float(data.get('total_higher_educated', 0))
    ]
    
    # Ensure the features are in the correct order as expected by the model
    prediction = random_regressor.predict([features])
    return jsonify(prediction.tolist())


if __name__ == '__main__':
    app.run(debug=True)