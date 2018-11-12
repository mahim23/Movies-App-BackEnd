from django.http import JsonResponse
from ..models import User, Movie, TV


def get_user_details(request, username):
    try:
        user = User.objects.get(pk=username)
        return JsonResponse(user, 200)
    except User.DoesNotExist:
        return JsonResponse({"message": "User with username={} not found".format(username)}, 400)


def like_movie(request):
    try:
        movie_id = request.POST["movie_id"]
        username = request.POST["username"]
        movie = Movie.objects.get(pk=movie_id)
        user = User.objects.get(pk=username)
    except KeyError:
        return JsonResponse({"message": "Incomplete data"}, 400)
    except (User.DoesNotExist, Movie.DoesNotExist):
        return JsonResponse({"message": "Invalid request"}, 400)
    if user.liked_movies.filter(pk=movie_id).exists():
        user.liked_movies.add(movie)
        response_message = "Movie added to favorites"
    else:
        user.liked_movies.remove(movie)
        response_message = "Movie removed from favorites"
    user.save()
    return JsonResponse({"message": response_message}, 200)


def like_tv(request):
    try:
        tv_id = request.POST["tv_id"]
        username = request.POST["username"]
        tv = TV.objects.get(pk=tv_id)
        user = User.objects.get(pk=username)
    except KeyError:
        return JsonResponse({"message": "Incomplete data"}, 400)
    except (User.DoesNotExist, TV.DoesNotExist):
        return JsonResponse({"message": "Invalid request"}, 400)
    if user.liked_tv.filter(pk=tv_id).exists():
        user.liked_tv.add(tv)
        response_message = "TV added to favorites"
    else:
        user.liked_tv.remove(tv)
        response_message = "TV removed from favorites"
    user.save()
    return JsonResponse({"message": response_message}, 200)
