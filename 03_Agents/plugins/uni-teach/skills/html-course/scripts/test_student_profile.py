"""Student-profile validation and rendering; fictional content only."""
import copy,json,unittest
import course
import test_course as fixtures
from test_course import draft_for,COURSE

class StudentProfileTests(unittest.TestCase):
    setUp = fixtures.ExportTests.setUp
    def student(self):
        snap=course.snapshot(self.vault,COURSE,['O001'])
        d=draft_for(snap);d['student_profile']=1
        l=d['lessons'][0]
        l['sections']=[{'id':i,'title':t,'html':'<p>Fictional study content.</p>'} for i,t in [('lesson-outline','Lesson outline'),('introduction','Introduction'),('definitions','Key definitions'),('practice','Practice'),('sources','Sources')]]
        l['sections'][3]['interactions']=[{'id':'mean-quiz','kind':'choice','prompt_html':'<h3 id="mean-check">4.1 Choices &amp; conditions</h3><p>Mean of1,2,3?</p>','choices':['1','2','3','6'],'correct_index':1,'feedback':['A single value omits the rest.','Sum6 divided by3 is2.','The maximum is not the mean.','Divide the sum by3.'],'solution_html':'<p>6/3=2.</p>'}]
        for e in d['coverage']:e['targets']=['o001#practice']
        return snap,d

    def test_valid_profile_context_and_navigation(self):
        snap,d=self.student();course.validate_draft(d,snap)
        nav=course.student_navigation(d)['o001']
        self.assertEqual(nav[0]['label'],'01 Lesson outline')
        self.assertEqual(next(x['label'] for x in nav if x['id']=='mean-check'),'4.1 Choices & conditions')
        page=course.page(d,'Quiz','<p>Body</p>',current='o001')
        self.assertIn('assets/student.js',page);self.assertIn('assets/student.css',page)
        self.assertIn('Divide the sum by3.',page)

    def test_agent_section_cannot_be_exposed_as_student(self):
        snap,d=self.student();d['lessons'][0]['sections'][2]['audience']='agent'
        with self.assertRaisesRegex(ValueError,'agent policies belong in metadata'):course.validate_draft(d,snap)

    def test_feedback_must_be_four_nonempty_strings_in_a_list(self):
        snap,d=self.student()
        for bad in ['abcd',['a','b','c'],['a','b','c',''],['a','b','c',None]]:
            x=copy.deepcopy(d);x['lessons'][0]['sections'][3]['interactions'][0]['feedback']=bad
            with self.subTest(bad=bad),self.assertRaises(ValueError):course.validate_draft(x,snap)

    def test_choices_must_be_four_distinct_visible_strings(self):
        snap,d=self.student()
        for bad in ['abcd',['a','b','c'],['a','b','c',''],['a','b','c',None],['a','<b>a</b>','c','d'],['a','a','c','d']]:
            x=copy.deepcopy(d);x['lessons'][0]['sections'][3]['interactions'][0]['choices']=bad
            with self.subTest(bad=bad),self.assertRaises(ValueError):course.validate_draft(x,snap)

    def test_answer_index_is_strict_integer(self):
        snap,d=self.student()
        for bad in [True,1.0,-1,4]:
            x=copy.deepcopy(d);x['lessons'][0]['sections'][3]['interactions'][0]['correct_index']=bad
            with self.subTest(bad=bad),self.assertRaises(ValueError):course.validate_draft(x,snap)

    def test_duplicate_interaction_ids_rejected_across_sections(self):
        snap,d=self.student();d['lessons'][0]['sections'][4]['interactions']=copy.deepcopy(d['lessons'][0]['sections'][3]['interactions'])
        with self.assertRaisesRegex(ValueError,'duplicate interaction ID'):course.validate_draft(d,snap)

    def test_outline_must_be_first(self):
        snap,d=self.student();d['lessons'][0]['sections'][:2]=reversed(d['lessons'][0]['sections'][:2])
        with self.assertRaisesRegex(ValueError,'outline must come first'):course.validate_draft(d,snap)

    def test_legacy_page_omits_student_runtime(self):
        snap=course.snapshot(self.vault,COURSE,['O001']);d=draft_for(snap)
        page=course.page(d,'Legacy','<p>Body</p>',current='o001')
        self.assertNotIn('student.js',page);self.assertNotIn('student.css',page)

if __name__=='__main__':unittest.main()
