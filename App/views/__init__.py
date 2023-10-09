# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .student import *
from .review import review_views
<<<<<<< HEAD

=======
>>>>>>> 0b7ecaf8eeed9c616440bdb380709ddf970a3f41


views = [user_views, index_views, auth_views, review_views] 
# blueprints must be added to this list
