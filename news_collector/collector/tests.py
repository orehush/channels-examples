import pytest
from channels.testing import HttpCommunicator
from .consumers import NewsCollectorAsyncConsumer


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_news_collector_consumer():
    communicator = HttpCommunicator(
        NewsCollectorAsyncConsumer,
        "GET",
        "/collector/collect_news_async/"
    )
    response = await communicator.get_response()
    assert response["status"] == 200
