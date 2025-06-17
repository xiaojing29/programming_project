from sac3 import paraphraser
from sac3.evaluator import Evaluate
from sac3.consistency_checker import SemanticConsistnecyCheck

# input information
# question = 'Was there ever a US senator that represented the state of Alabama and whose alma mater was MIT?'
# question = 'Did Brazil win the gold medal for Women volleyball at the 2016 Summer Olympics?'
question = 'Does a drug interaction exists between Covid antiviral pill Paxlovid and the blood-pressure-lowering medication verapamil?'
target_answer = 'Yes'

# question pertubation
gen_question = paraphraser.paraphrase(question, number = 3, model = 'gpt-3.5-turbo', temperature=1.0)
# gen_question = paraphraser.paraphrase(question, number = 3, model = 'guanaco-33b', temperature=1.0)
print(gen_question)

# llm evaluation
llm_evaluate = Evaluate(model='gpt-3.5-turbo')
# llm_evaluate = Evaluate(model='guanaco-33b')
self_responses = llm_evaluate.self_evaluate(self_question = question, temperature = 1.0, self_num = 3)
perb_responses = llm_evaluate.perb_evaluate(perb_questions = gen_question, temperature=0.0)
print(self_responses)
print(perb_responses)

# consistency check 
scc = SemanticConsistnecyCheck(model='gpt-3.5-turbo')
# scc = SemanticConsistnecyCheck(model='guanaco-33b')

sc2_score, sc2_vote = scc.score_scc(question, target_answer, candidate_answers = self_responses, temperature = 0.0)
print(sc2_score, sc2_vote)

sac3_q_score, sac3_q_vote = scc.score_scc(question, target_answer, candidate_answers = perb_responses, temperature = 0.0)
print(sac3_q_score, sac3_q_vote)