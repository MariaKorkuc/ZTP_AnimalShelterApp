from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status

from AnimalShelterApp.models import Animal

class PostListCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('api-post-list', kwargs={'version': 'v1'})

    def test_create_post(self):
        self.assertEquals(
            Post.objects.count(),
            0
        )
        data = {
            'title': 'title',
            'text': 'text'
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            Post.objects.count(),
            1
        )
        post = Post.objects.first()
        self.assertEquals(
            post.title,
            data['title']
        )
        self.assertEquals(
            post.text,
            data['text']
        )

    def test_get_post_list(self):
        tag = Tag(name='tag_name')
        tag.save()
        post = Post(title='title1', text='text1')
        post.save()
        post.tags.add(tag)

        response = self.client.get(self.url)
        response_json = response.json()
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            len(response_json),
            1
        )
        data = response_json[0]
        self.assertEquals(
            data['title'],
            post.title
        )
        self.assertEquals(
            data['text'],
            post.text
        )
        self.assertEquals(
            data['tags'][0]['name'],
            tag.name
        )
