---
layout: page
permalink: /publications/
title: publications
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<!-- Filter Feature -->
<div class="filters" style="text-align: left;">
  <div class="filter-item type-selector">
    <label for="typeSelect">Select a Publication Type: </label>
    <div class="custom-select-wrapper">
      <select id="typeSelect" onchange="filterPublications()">
        <option value="all">All Types</option>
        <option value="article">Article</option>
        <option value="conference">Conference Papers</option>
        <option value="book">Book Chapters</option>
        <option value="thesis">Theses</option>
        <!-- Add more types as needed -->
      </select>
    </div>
  </div>
</div>

<script>
function filterPublications() {
  const selectedType = document.getElementById('typeSelect').value;
  const entries = document.querySelectorAll('.row .col-sm-8');

  entries.forEach(entry => {
    const entryType = entry.getAttribute('data-type');

    // Check if the entry matches the selected filter
    const matchType = selectedType === 'all' || entryType === selectedType;

    // Show or hide the entry based on filter match
    entry.parentElement.style.display = matchType ? '' : 'none';
  });
}
</script>

<div class="publications">

{% bibliography %}

</div>

<style>
  .filters {
    display: flex;
    flex-direction: row;
    gap: 20px;
    align-items: flex-start; /* Aligns items to the left */
    max-width: 300px;
    margin: 0; /* Adjust or remove margin as needed */
  }

  .custom-select-wrapper {
    position: relative;
    width: 100%;
  }

  select {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
    appearance: none; /* Removes default styling of select */
    background-color: #f9f9f9;
  }

  .custom-select-wrapper:after {
    content: "\25BC"; /* Adds custom arrow */
    position: absolute;
    top: 50%;
    right: 15px;
    transform: translateY(-50%);
    pointer-events: none;
    color: #777;
  }

  label {
    font-weight: bold;
    margin-bottom: 5px;
    display: block;
  }
</style>