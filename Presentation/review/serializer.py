from rest_framework import serializers

from Context.review.domain.member_review import MemberReviewAggregate

S3_ORIGIN_ABSOLUTE_PATH = "https://storage.we-marry.com.s3.ap-northeast-2.amazonaws.com"
ROUTE_53_S3_PATH = "http://storage.we-marry.com"


class ReviewSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = MemberReviewAggregate
        fields = ["member_id", "type", "file", "status"]

    def get_file(self, obj: MemberReviewAggregate) -> str:
        file_path: str = obj.file.url.replace(S3_ORIGIN_ABSOLUTE_PATH, ROUTE_53_S3_PATH)
        return file_path
