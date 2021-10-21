class Config:
    SECRET_KEY = '83sCG5nbDXXR#-+ghVPKLRh9837_$'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///store.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass
