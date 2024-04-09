from flask import Flask, request, jsonify,render_template
import joblib

app = Flask(__name__)
random_regressor = joblib.load('random_forest_regressor.pkl')  # Load your trained Random Forest model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        less_than_9th_grade,
        percent_less_than_9th_grade,
        ninth_to_twelfth,
        percent_ninth_to_twelfth,
        highschool_grad,
        percent_highschool_grad,
        some_college_no_degree,
        percent_some_college_no_degree,
        associates_degree,
        percent_associates_degree,
        bachelors_degree,
        percent_bachelors_degree,
        graduate_degree,
        percent_graduate_degree,
        Total_population,
        under_five,
        percent_under_five,
        five_to_nine,
        percent_five_to_nine,
        ten_to_fourteen,
        percent_ten_to_fourteen,
        fifteen_to_nineteen,
        percent_fifteen_to_nineteen,
        twenty_to_twentyfour,
        percent_twenty_to_twentyfour,
        twentyfive_to_thirtyfour,
        percent_twentyfive_to_thirtyfour,
        thirtyfive_to_fourtyfour,
        percent_thirtyfive_to_fourtyfour,
        fourtyfive_to_fiftyfour,
        percetnt_fourtyfive_to_fiftyfour,
        fiftyfive_to_fiftynine,
        percent_fiftyfive_to_fiftynine,
        sixty_to_sixtyfour,
        percent_sixty_to_sixtyfour,
        sixtyfive_to_seventyfour,
        percent_sixtyfive_to_seventyfour,
        seventyfive_to_eightyfour,
        percent_seventyfive_to_eightyfour,
        over_eigtyfive,
        percent_over_eigtyfive,
        unemployment_rate,
        income,
        house_price,
        percent_poverty,
        total_homes,
        owner_occupied,
        renter_occupied,
        percent_owner_occupied,
        percent_renter_occupied,
        percent_over_twentyfive,
        percent_under_fourteen,
        percent_young_adults,
        percent_uneducated,
        percent_higher_education,
        total_uneducated,
        total_higher_educated
    ]
    prediction = random_regressor.predict(features)
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(debug=True)