from rest_framework.routers import SimpleRouter
from rest_framework_extensions.routers import NestedRouterMixin

import posts.views as views


class NestedSimpleRouter(NestedRouterMixin, SimpleRouter):
    pass


router = NestedSimpleRouter()
posts_router = router.register('posts', views.PostViewSet, base_name='posts')
posts_router.register('comments', views.CommentViewSet, base_name='post_comments', parents_query_lookups=['post'])
posts_router.register('likes', views.LikeViewSet, base_name='post_likes', parents_query_lookups=['post'])

app_name = 'posts'
urlpatterns = []
urlpatterns += router.urls
