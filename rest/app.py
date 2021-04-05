from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SECRET_KEY'] = "12052003"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:12052003@localhost/circus-shows-db"
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Performance(db.Model):
    __tablename__ = 'performance'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)
    musicians_number = db.Column(db.Integer, unique=False, nullable=False)
    avg_ticket_price = db.Column(db.Integer, unique=False, nullable=False)

class PerformanceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'musicians_number', 'avg_ticket_price')


@app.route("/", methods=["GET"])
def get_performances():
    performances = Performance.query.all()
    return jsonify(PerformanceSchema(many=True).dump(performances))


@app.route("/<id>", methods=["GET"])
def get_performance(id):
    performance = Performance.query.get(id)
    if not performance:
        abort(404)
    return jsonify(PerformanceSchema().dump(performance))


@app.route("/", methods=["POST"])
def add_bear():
    performance = Performance(name=request.json["name"], musicians_number=request.json["musicians_number"], avg_ticket_price=request.json["avg_ticket_price"])
    db.session.add(performance)
    db.session.commit()
    return jsonify(PerformanceSchema().dump(performance))


@app.route("/<id>", methods=["DELETE"])
def delete_performance(id):
    performance = Performance.query.get(id)
    if not performance:
        abort(404)
    db.session.delete(performance)
    db.session.commit()
    return jsonify(success=True)


@app.route("/<id>", methods=["PUT"])
def update_performance(id):
    performance = Performance.query.get(id)
    if not performance:
        abort(404)
    performance.name = request.json["name"]
    performance.musicians_number = request.json["musicians_number"]
    performance.avg_ticket_price = request.json["avg_ticket_price"]
    db.session.commit()
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)
