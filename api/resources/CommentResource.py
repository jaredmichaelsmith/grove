"""CommentResource.py"""


import uuid

from flask.ext.restful import Resource, reqparse, current_app

from api.documents import Comment, HammockLocation
from api.utils import abort_not_exist, require_login


class CommentResource(Resource):
    """Comment Resource class"""

    def __init__(self):
        self.put_parser = self.setup_put_parser()
        self.post_parser = self.setup_post_parser()

    def setup_post_parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str)
        parser.add_argument('location_id', required=True, type=str)
        return parser

    def setup_put_parser(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', required=True, type=str)
        return parser

    @require_login
    def get(self, user, location_uuid):
        current_app.logger.debug(user.to_json())
        location = HammockLocation.objects(uuid=location_uuid).first()
        if location is None:
            abort_not_exist(location_uuid, 'Location')

        encoded_comments = []
        for comment in location.comments:
            encoded_comments.append(comment.to_json())

        return encoded_comments

    @require_login
    def post(self, user):
        current_app.logger.debug(user.to_json())
        parsed_args = self.post_parser.parse_args()

        comment = Comment(text=parsed_args['text'],
                          location_uuid=parsed_args['location_id'],
                          user_uuid=user.uuid,
                          uuid=str(uuid.uuid4()))

        HammockLocation.objects(
            uuid=parsed_args['location_id']).update_one(push__comments=comment)

        return comment.to_json()

    @require_login
    def put(self, user, comment_id=None):
        current_app.logger.debug(user.to_json())
        parsed_args = self.put_parser.parse_args()

        comment = Comment.objects(uuid=comment_id).first()
        if comment is None:
            abort_not_exist(comment_id, 'Comment')

        comment.update(text=parsed_args['text'])
        comment.save()

        return comment.to_json()
