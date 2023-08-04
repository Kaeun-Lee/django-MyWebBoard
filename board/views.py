from django.shortcuts import render, get_object_or_404

from .models import Boards


def index(request):
    board_obj = Boards.objects.all().order_by("-created_date")
    context = {"post_list": board_obj}
    return render(request, "board/index.html", context)


def detail(request, board_id):
    post = get_object_or_404(Boards, pk=board_id)
    context = {"post_detail": post}
    return render(request, "board/detail.html", context)
