from django.shortcuts import render, get_object_or_404, redirect

from .models import Boards


# READ
def index(request):
    board_obj = Boards.objects.all().order_by("-created_date")
    context = {"post_list": board_obj}
    return render(request, "board/index.html", context)


# READ
def detail(request, board_id):
    post = get_object_or_404(Boards, pk=board_id)
    context = {"post_detail": post}
    return render(request, "board/detail.html", context)


def write(request):  # 글쓰기 페이지로 이동
    return render(request, "board/write.html")


# CREATE
def create_post(request):
    new_board = Boards()  # 데이터 저장을 위한 객체 생성
    new_board.title = request.POST["title"]
    new_board.content = request.POST["content"]
    new_board.writer = request.POST["writer"]
    new_board.save()  # 객체 저장
    return redirect("board:index")
