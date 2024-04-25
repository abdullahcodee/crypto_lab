from flask import render_template, redirect, url_for, flash
from .forms import ResearchForm
from .models import Research
from app import db
from flask import Blueprint


researcher_bp = Blueprint('researcher', __name__, template_folder='templates')

@researcher_bp.route('/research', methods=['GET', 'POST'])
def research():
    form = ResearchForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        research = Research(title=title, content=content)
        db.session.add(research)
        db.session.commit()
        flash('Your research has been posted!', 'success')
        return redirect(url_for('researcher.research'))
    return render_template('researcher/home.html', form=form)

@researcher_bp.route('/research/<int:research_id>')
def research_detail(research_id):
    research = Research.query.get_or_404(research_id)
    return render_template('researcher/research.html', research=research)

@researcher_bp.route('/research/<int:research_id>/comments', methods=['GET', 'POST'])
def research_comments(research_id):
    research = Research.query.get_or_404(research_id)
    # Add comment functionality here
    return render_template('researcher/comments.html', research=research)
