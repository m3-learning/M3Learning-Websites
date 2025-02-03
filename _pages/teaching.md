---
layout: page
permalink: /teaching/
title: Teaching
description: A collection of courses taught.
nav_order: 6
display_categories: [year, university, topics]
---

<!-- Dropdown Filters -->
<div class="filters">
  <label for="filter-year">Filter by Year:</label>
  <select id="filter-year">
    <option value="all">All</option>
    {% assign years = site.teaching | map: "year" | uniq | sort %}
    {% for year in years %}
      <option value="{{ year }}">{{ year }}</option>
    {% endfor %}
  </select>

  <label for="filter-university">Filter by University:</label>
  <select id="filter-university">
    <option value="all">All</option>
    {% assign universities = site.teaching | map: "university" | uniq | sort %}
    {% for university in universities %}
      <option value="{{ university }}">{{ university }}</option>
    {% endfor %}
  </select>

  <label for="filter-topics">Filter by Topic:</label>
  <select id="filter-topics">
    <option value="all">All</option>
    {% assign topics = site.teaching | map: "topics" | join: ',' | split: ',' | uniq | sort %}
    {% for topic in topics %}
      <option value="{{ topic }}">{{ topic }}</option>
    {% endfor %}
  </select>
</div>

<!-- Course Listing -->
<div class="row row-cols-1 row-cols-md-3" id="course-list">
  {% for course in site.teaching %}
    {% include teaching.liquid course=course %}
  {% endfor %}
</div>

<!-- JavaScript for Filtering -->
<script>
  document.addEventListener('DOMContentLoaded', function () {
    const yearFilter = document.getElementById('filter-year');
    const universityFilter = document.getElementById('filter-university');
    const topicFilter = document.getElementById('filter-topics');
    const courses = document.querySelectorAll('.course-card');

    function filterCourses() {
      const selectedYear = yearFilter.value;
      const selectedUniversity = universityFilter.value;
      const selectedTopic = topicFilter.value;

      courses.forEach(course => {
        const courseYear = course.getAttribute('data-year');
        const courseUniversity = course.getAttribute('data-university');
        const courseTopics = course.getAttribute('data-topics').split(',');

        const matchesYear = (selectedYear === 'all' || courseYear === selectedYear);
        const matchesUniversity = (selectedUniversity === 'all' || courseUniversity === selectedUniversity);
        const matchesTopic = (selectedTopic === 'all' || courseTopics.includes(selectedTopic));

        if (matchesYear && matchesUniversity && matchesTopic) {
          course.style.display = 'block';
        } else {
          course.style.display = 'none';
        }
      });
    }

    yearFilter.addEventListener('change', filterCourses);
    universityFilter.addEventListener('change', filterCourses);
    topicFilter.addEventListener('change', filterCourses);
  });
</script>

