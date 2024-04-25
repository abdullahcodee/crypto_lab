from app import db

class CipherResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_text = db.Column(db.String(255), nullable=False)
    cipher_text = db.Column(db.String(255), nullable=False)
    method = db.Column(db.String(50), nullable=False)
    action = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<CipherResult {self.id}>"
