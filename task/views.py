from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import Account
from django.db.models import Max
from django.http import JsonResponse
from .models import Workspace, Board, List, Card, CardAttachment, CommentCard
from .forms import *

# Create your views here.
def create_workspace(request):
    url = request.META.get('HTTP_REFERER') 
    user_login = get_object_or_404(Account, id=request.user.id)
    
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        data = Workspace()
        data.title = title
        data.description = description
        data.user_create = user_login
        data.save()
        return redirect(url)
    
def board_workspace(request, workspace_id, favorite=None):
    user_Login = get_object_or_404(Account, id=request.user.id)
    workspaces = Workspace.objects.all().filter(user_create=user_Login)
    
    workspace = get_object_or_404(Workspace, id=workspace_id)
        
    if favorite != None:
        boards = Board.objects.all().filter(workspace=workspace, favorite=True)
    else:
        boards = Board.objects.all().filter(workspace=workspace)

    context = {
        'workspaces' : workspaces,
        'workspace' : workspace,
        'boards' : boards,
        'favorite' : favorite,
    }
    
    return render(request, 'task/board_workspace.html', context)

def board_favorite(request, id_board, status):
    url = request.META.get('HTTP_REFERER') 
    board = get_object_or_404(Board, id=id_board)
    board.favorite = status
    board.save()
    return redirect(url)

def create_board(request, id_workspace):
    url = request.META.get('HTTP_REFERER') 
    workspace = get_object_or_404(Workspace, id=id_workspace)
    user_login = get_object_or_404(Account, id=request.user.id)
    
    if request.method == 'POST':
        board = Board()
        title_board = request.POST['title_board']
        board.title_board = title_board
        board.workspace = workspace
        board.user_board = user_login
        board.save()
        
    return redirect(url)

def view_board(request, id_board):
    
    card_form = CardForm()
    file_form = CardAttachmentForm()
    
    board = get_object_or_404(Board, id=id_board)
    
    lists = List.objects.all().filter(board=board).order_by('position')
    cards = Card.objects.filter(list__id__in = lists).order_by('position')
    
    user = get_object_or_404(Account, id=request.user.id)
    workspaces = Workspace.objects.all().filter(user_create=user)
    
    context ={
        'board' : board,
        'lists' : lists,
        'card_form' : card_form,
        'cards' : cards,
        'file_form' : file_form,
        'workspaces' : workspaces,
    }
    return render(request, 'task/view_board.html', context)

def create_list(request, id_board):
    url = request.META.get('HTTP_REFERER') 
    user_Login = get_object_or_404(Account, id=request.user.id)
    board = get_object_or_404(Board, id=id_board)
    
    max_position = List.objects.filter(board=board).aggregate(max_valor=Max('position'))
    max_position = max_position['max_valor']
       
    if max_position:
        max_position += 1
    else:
        max_position = 1
    
    if request.method == "POST":
        list_title = request.POST['list_title']
        lists = List()  
        lists.list_title = list_title  
        lists.board = board 
        lists.user_list = user_Login
        lists.position = max_position
        lists.save()
        
        return redirect(url)

def move_card(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        new_list_id = request.POST.get('new_list_id')
        
        try:
            card = Card.objects.get(id=card_id)
            new_list = List.objects.get(id=new_list_id)
            
            card.list = new_list
            card.save()
            # Devuelve los datos actualizados de la tarjeta en la respuesta JSON
            return JsonResponse({'message': 'Card moved successfully', 'updated_card_id': card.id})
        except Card.DoesNotExist:
            return JsonResponse({'error': 'The card does not exist.'})
        except List.DoesNotExist:
            return JsonResponse({'error': 'The list does not exist.'})
    
    return JsonResponse({'error': 'Disallowed method.'})

def update_title_board(request):
    if request.method == 'POST':
        board_id = request.POST.get('board_id')
        new_value = request.POST.get('new_value')
        try:
            board = Board.objects.get(id=board_id)
            board.title_board = new_value
            board.save()

            return JsonResponse({'success': True})
        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'The board does not exist.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Error updating board.'})

    return JsonResponse({'success': False, 'error': 'Disallowed method.'})

def update_title_list(request):
    if request.method == 'POST':
        list_id = request.POST.get('list_id')
        new_value = request.POST.get('new_value')
        try:
            lists = List.objects.get(id=list_id)
            lists.list_title = new_value
            lists.save()

            return JsonResponse({'success': True})
        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'The list does not exist.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Error updating list.'})

    return JsonResponse({'success': False, 'error': _('Disallowed method.')})

def update_title(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        new_value = request.POST.get('new_value')
        try:
            card = Card.objects.get(id=card_id)
            card.card_title = new_value
            card.save()

            return JsonResponse({'success': True})
        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'The card does not exist.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Error updating card.'})

    return JsonResponse({'success': False, 'error': 'Disallowed method.'})

def update_title_list(request):
    if request.method == 'POST':
        list_id = request.POST.get('list_id')
        new_value = request.POST.get('new_value')
        try:
            lists = List.objects.get(id=list_id)
            lists.list_title = new_value
            lists.save()

            return JsonResponse({'success': True})
        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'The list does not exist.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Error updating list.'})

    return JsonResponse({'success': False, 'error': 'Disallowed method.'})

def update_description(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        new_value = request.POST.get('new_value')
        try:
            card = Card.objects.get(id=card_id)
            card.card_description = new_value
            card.save()

            return JsonResponse({'success': True})
        except Card.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'The card does not exist.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Error updating card.'})

    return JsonResponse({'success': False, 'error': 'Disallowed method.'})  

def list_delete(request, list_id):
    url = request.META.get('HTTP_REFERER') 
    list_select = get_object_or_404(List, id=list_id)
    list_select.delete()  
    return redirect(url)

def update_list_order(request):
    if request.method == 'POST':
        new_list_order = request.POST.getlist('new_list_order[]') 

        try:
            for idx, list_id in enumerate(new_list_order, start=1):
                List.objects.filter(id=list_id).update(position=idx)
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error_message': str(e)})

    return JsonResponse({'success': False, 'error_message': 'Método no permitido'})

def create_card(request, id_list):
    url = request.META.get('HTTP_REFERER') 
    user_login = get_object_or_404(Account, id=request.user.id)
    list_select = get_object_or_404(List, id=id_list)
    
    if request.method == "POST":
        card_form = CardForm(request.POST, request.FILES)
        card_file_form = CardAttachmentForm(request.POST, request.FILES)
        
        if card_form.is_valid() and card_file_form.is_valid():
            
            card = Card(
                card_title = card_form.cleaned_data['card_title'],
                card_description = card_form.cleaned_data['card_description'],
                file_imagen = card_form.cleaned_data['file_imagen'],
                list = list_select,
                user_card = user_login
            )
            
            card.save()
            
            file = card_file_form.cleaned_data['file']
            
            if file:
                card_file = CardAttachment (
                    card = card,
                    file = card_file_form.cleaned_data['file']
                    
                )
                card_file.save()
            
                #card.attachments.add(card_file)
            
            
            
    return redirect(url)








