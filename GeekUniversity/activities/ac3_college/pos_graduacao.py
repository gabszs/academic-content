class PosGraduacao ():

    def __init__(self, instituicao, curso):

        self.instituicao = instituicao
        self.curso = curso

    def get_curso(self):
        pass
        # na subclasse retornáza a string 'doutorado en nome do curso.

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        self._curso = curso.Title()



class Doutorado(PosGraduacao):
    pass
    '''def __init__(self, tese=None):
        Doutorado.__tese = tese'''





dot = Doutorado('impacta', 'eng_comp')
print(dot.instituicao, dot.curso)