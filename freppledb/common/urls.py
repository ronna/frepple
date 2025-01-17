#
# Copyright (C) 2007-2017 by frePPLe bv
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.urls import re_path
from django.views.generic.base import RedirectView

import freppledb.common.views
import freppledb.common.serializers
import freppledb.common.dashboard

from freppledb.common.api.views import APIIndexView
from freppledb.common.registration.views import (
    ResetPasswordRequestView,
    PasswordResetConfirmView,
)


# Automatically add these URLs when the application is installed
autodiscover = True

urlpatterns = [
    re_path(r"^uploads/(.+)$", freppledb.common.views.uploads, name="uploads"),
    re_path(r"^inbox/$", freppledb.common.views.inbox, name="inbox"),
    re_path(r"^follow/$", freppledb.common.views.follow, name="follow"),
    re_path(r"^$", freppledb.common.views.cockpit, name="cockpit"),
    re_path(r"^preferences/$", freppledb.common.views.preferences, name="preferences"),
    re_path(r"^horizon/$", freppledb.common.views.horizon, name="horizon"),
    re_path(r"^settings/$", freppledb.common.views.saveSettings),
    re_path(
        r"^widget/(.+)/",
        freppledb.common.dashboard.Dashboard.dispatch,
        name="dashboard",
    ),
    # Model list reports, which override standard admin screens
    re_path(r"^data/login/$", freppledb.common.views.login),
    re_path(
        r"^data/auth/group/$",
        freppledb.common.views.GroupList.as_view(),
        name="auth_group_changelist",
    ),
    re_path(
        r"^data/common/user/$",
        freppledb.common.views.UserList.as_view(),
        name="common_user_changelist",
    ),
    re_path(
        r"^data/common/follower/$",
        freppledb.common.views.FollowerList.as_view(),
        name="common_follower_changelist",
    ),
    re_path(
        r"^data/common/bucket/$",
        freppledb.common.views.BucketList.as_view(),
        name="common_bucket_changelist",
    ),
    re_path(
        r"^data/common/bucketdetail/$",
        freppledb.common.views.BucketDetailList.as_view(),
        name="common_bucketdetail_changelist",
    ),
    re_path(
        r"^data/common/parameter/$",
        freppledb.common.views.ParameterList.as_view(),
        name="common_parameter_changelist",
    ),
    re_path(
        r"^data/common/attribute/$",
        freppledb.common.views.AttributeList.as_view(),
        name="common_attribute_changelist",
    ),
    re_path(
        r"^data/common/comment/$",
        freppledb.common.views.CommentList.as_view(),
        name="common_comment_changelist",
    ),
    # Special case of the next line for user password changes in the user edit screen
    re_path(
        r"detail/common/user/(?P<id>.+)/password/$",
        RedirectView.as_view(url="/data/common/user/%(id)s/password/"),
    ),
    # Detail URL for an object, which internally redirects to the view for the last opened tab
    re_path(r"^detail/([^/]+)/([^/]+)/(.+)/$", freppledb.common.views.detail),
    # REST API framework
    re_path(r"^api/common/bucket/$", freppledb.common.serializers.BucketAPI.as_view()),
    re_path(
        r"^api/common/bucketdetail/$",
        freppledb.common.serializers.BucketDetailAPI.as_view(),
    ),
    re_path(
        r"^api/common/bucketdetail/$",
        freppledb.common.serializers.BucketDetailAPI.as_view(),
    ),
    re_path(
        r"^api/common/parameter/$", freppledb.common.serializers.ParameterAPI.as_view()
    ),
    re_path(
        r"^api/common/attribute/$", freppledb.common.serializers.AttributeAPI.as_view()
    ),
    re_path(
        r"^api/common/comment/$", freppledb.common.serializers.CommentAPI.as_view()
    ),
    re_path(
        r"^api/common/bucket/(?P<pk>(.+))/$",
        freppledb.common.serializers.BucketdetailAPI.as_view(),
    ),
    re_path(
        r"^api/common/bucketdetail/(?P<pk>(.+))/$",
        freppledb.common.serializers.BucketDetaildetailAPI.as_view(),
    ),
    re_path(
        r"^api/common/parameter/(?P<pk>(.+))/$",
        freppledb.common.serializers.ParameterdetailAPI.as_view(),
    ),
    re_path(
        r"^api/common/attribute/(?P<pk>(.+))/$",
        freppledb.common.serializers.AttributedetailAPI.as_view(),
    ),
    re_path(
        r"^api/common/comment/(?P<pk>(.+))/$",
        freppledb.common.serializers.CommentdetailAPI.as_view(),
    ),
    re_path(r"^api/$", APIIndexView),
    re_path(r"^about/$", freppledb.common.views.AboutView, name="about"),
    re_path(r"^scenarios/$", freppledb.common.views.ScenarioView, name="scenarios"),
    # Forgotten password
    re_path(
        r"^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$",
        PasswordResetConfirmView.as_view(),
        name="reset_password_confirm",
    ),
    re_path(
        r"^reset_password/$", ResetPasswordRequestView.as_view(), name="reset_password"
    ),
]
