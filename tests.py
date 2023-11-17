from heredity import joint_probability, get_person_probability, probability_from_PROBS


def test_joint_probability_family():

    people = {}
    people["Harry"] = {
                    "name": "Harry",
                    "mother": "Lily",
                    "father": "James",
                    "trait": 0
                }
    people["James"] = {
                    "name": "James",
                    "mother": None,
                    "father": None,
                    "trait": 1
                }
    people["Lily"] = {
                    "name": "Lily",
                    "mother": None,
                    "father": None,
                    "trait": 0
                }

    one_gene = {"Harry"}
    two_genes = {"James"}
    have_trait = {"James"}
    joint_p = joint_probability(people, one_gene, two_genes, have_trait)

    assert joint_p == 0.0026643247488



def test_joint_probability_parents():
    people = {}
    people["Lily"] = {
                    "name": "Lily",
                    "mother": None,
                    "father": None,
                    "trait": 0
                }
    assert round(probability_from_PROBS(people["Lily"], set(), set(), False), 4) == 0.9504
    assert round(joint_probability(people, set(), set(), set()), 4) == 0.9504

    people_2 = {}
    people_2["James"] = {
                    "name": "James",
                    "mother": None,
                    "father": None,
                    "trait": 1
                }
    assert round(joint_probability(people_2, set(), {"James"}, {"James"}), 4) == 0.0065



def test_Harry_probability():
    people = {}
    people["Harry"] = {
                    "name": "Harry",
                    "mother": "Lily",
                    "father": "James",
                    "trait": 0
                }
    people["James"] = {
                    "name": "James",
                    "mother": None,
                    "father": None,
                    "trait": 1
                }
    people["Lily"] = {
                    "name": "Lily",
                    "mother": None,
                    "father": None,
                    "trait": 0
                }

    one_gene = {"Harry"}
    two_genes = {"James"}
    have_trait = {"James"}


    assert get_person_probability(people, "Harry", one_gene, two_genes, have_trait) == 0.431288


