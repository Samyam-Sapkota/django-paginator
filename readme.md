<h1>First add followin in the views.py </h1>

<h2>
    paginator = Paginator(models_queryset, number of page )  # eg : Paginator(models_queryset, 10)
    page_numer = request.GET.get('page')  # to fech the page number from the request
    page_object = paginator.get_page(page_numer) # to get the page object

    #then render the page object in the template by passing it to the context
</h2>



<h1>Then in the template add following line of code from line number 18 to 79</h1>



<!-->
{% if page_object.paginator.num_pages > 1 %}
<div class="flex justify-center mt-8">
  <nav class="flex items-center space-x-1 bg-white rounded-lg shadow-sm border border-gray-200 p-1">
    {% if page_object.has_previous %}
      <a href="?page={{ page_object.previous_page_number }}" 
         class="flex items-center px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 hover:text-gray-900 transition-all duration-200 hover:shadow-sm">
        <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
        </svg>
        Previous
      </a>
    {% else %}
      <span class="flex items-center px-3 py-2 text-sm font-medium text-gray-400 bg-gray-50 border border-gray-200 rounded-md cursor-not-allowed">
        <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
        </svg>
        Previous
      </span>
    {% endif %}

    <div class="flex items-center space-x-1 mx-2">
      {% for num in page_object.paginator.page_range %}
        {% if num == 1 or num == page_object.paginator.num_pages or num >= page_object.number|add:'-2' and num <= page_object.number|add:'2' %}
          {% if num == page_object.number %}
            <span class="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-white bg-gradient-to-r from-blue-600 to-blue-700 rounded-md shadow-sm ring-1 ring-blue-600">
              {{ num }}
            </span>
          {% else %}
            <a href="?page={{ num }}" 
               class="relative inline-flex items-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 hover:text-gray-900 hover:border-gray-400 transition-all duration-200 hover:shadow-sm">
              {{ num }}
            </a>
          {% endif %}
        {% elif num == page_object.number|add:'-3' or num == page_object.number|add:'3' %}
          <span class="relative inline-flex items-center px-2 py-2 text-sm font-medium text-gray-400">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z"/>
            </svg>
          </span>
        {% endif %}
      {% endfor %}
    </div>

    {% if page_object.has_next %}
      <a href="?page={{ page_object.next_page_number }}" 
         class="flex items-center px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 hover:text-gray-900 transition-all duration-200 hover:shadow-sm">
        Next
        <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </a>
    {% else %}
      <span class="flex items-center px-3 py-2 text-sm font-medium text-gray-400 bg-gray-50 border border-gray-200 rounded-md cursor-not-allowed">
        Next
        <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
        </svg>
      </span>
    {% endif %}
  </nav>
</div>
{% endif %}
-->

<h1>Thank yoou </h1>