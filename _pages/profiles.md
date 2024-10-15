---
layout: page
permalink: /team
title: team
description: Meet the current and past members of the m3-learning reserach group.
nav: true
nav_rank: 2
---

{% if site.data.members %}

  {% assign groups = site.data.members | sort: "group_rank" | map: "group" | uniq %}
  
  {% for group in groups %}

  <h2>{{ group }}</h2>

  <div class="group-section">
      {% assign members = site.data.members | where: "group", group %}
      {% if group contains "Alumni" %}
          {% assign members_with_end_year = members | where_exp: "member", "member.profile.end_year" %}
          {% assign members_without_end_year = members | where_exp: "member", "member.profile.end_year == nil" %}
          {% assign members_with_end_year = members_with_end_year | sort: "profile.end_year" | reverse %}
          {% assign members = members_with_end_year | concat: members_without_end_year %}
      {% else %}
          {% assign members = members | sort: "start_date" | reverse %}
      {% endif %}
      
      {% for member in members %}
      <div class="member-section">
          <p>
              <div class="card {% if member.inline == false %}hoverable{% endif %}">
                  <div class="row no-gutters">
                      <!-- Add 'd-flex align-items-center' classes here -->
                      <div class="col-sm-4 col-md-3 d-flex align-items-center">
                          <img src="{{ '/assets/img/people/' | append: member.profile.image | relative_url }}" class="card-img img-fluid" alt="{{ member.profile.name }}" />
                      </div>
                      <div class="team col-sm-8 col-md-9">
                          <div class="card-body">
                              {% if member.inline == false %}<a href="{{ member.url | relative_url }}">{% endif %}
                              <h5 class="card-title">{{ member.profile.name }}</h5>
                              {% if member.profile.position %}<h6 class="card-subtitle mb-2 text-muted">{{ member.profile.position }}</h6>{% endif %}
                              {% if member.profile.project %}
                                  <p class="card-text">
                                      <strong>Project:</strong> {{ member.profile.project }}
                                  </p>
                              {% endif %}
                              {% if member.profile.degrees %}
                                  <p class="card-text">
                                      {% assign degrees = member.profile.degrees %}
                                      {% for degree in degrees %}
                                            {{ degree }} <br />
                                      {% endfor %}
                                  </p>
                              {% endif %}
                              {% if member.profile.primary_advisor %}
                                <p class="card-text">
                                    <strong>Primary Advisor:</strong> {{ member.profile.primary_advisor }}
                                </p>
                              {% endif %}

                              {% if member.profile.coadvisor %}
                                <p class="card-text">
                                    <strong>Co-Advisor:</strong> {{ member.profile.coadvisor }}
                                </p>
                              {% endif %}

                              {% if member.profile.awards %}
                                <p class="card-text">
                                    <strong>Awards:</strong>
                                    <ul>
                                    {% for award in member.profile.awards %}
                                        <li>{{ award }}</li>
                                    {% endfor %}
                                    </ul>
                                </p>
                              {% endif %}
                              {% if group contains "Alumni" %}
                                  {% if member.profile.end_year %}
                                      <p class="card-text">
                                          {{ member.profile.start_year }} - {{ member.profile.end_year }}
                                      </p>
                                  {% endif %}
                                  {% if member.profile.current_position %}
                                      <p class="card-text">
                                          <strong>Current Position:</strong> {{ member.profile.current_position }}
                                      </p>
                                  {% endif %}
                              {% else %}
                                  {% if member.profile.start_year %}
                                      <p class="card-text">
                                          {{ member.profile.start_year }} - Present
                                      </p>
                                  {% endif %}
                              {% endif %}
                              <p class="card-text">
                                  {{ member.teaser }}
                              </p>
                              {% if member.inline == false %}</a>{% endif %}
                              <div class="contact-info">
                                  {% if member.profile.email %}
                                      <a href="mailto:{{ member.profile.email }}" class="card-link"><i class="fas fa-envelope"></i></a>
                                  {% endif %}
                                  {% if member.profile.phone %}
                                      <a href="tel:{{ member.profile.phone }}" class="card-link"><i class="fas fa-phone"></i></a>
                                  {% endif %}
                                  {% if member.profile.linkedin %}
                                      <a href="https://linkedin.com/in/{{ member.profile.linkedin }}/" class="card-link" target="_blank"><i class="fab fa-linkedin"></i></a>
                                  {% endif %}
                                  {% if member.profile.orcid %}
                                      <a href="https://orcid.org/{{ member.profile.orcid }}" class="card-link" target="_blank"><i class="fab fa-orcid"></i></a>
                                  {% endif %}
                                  {% if member.profile.twitter %}
                                      <a href="https://twitter.com/{{ member.profile.twitter }}" class="card-link" target="_blank"><i class="fab fa-twitter"></i></a>
                                  {% endif %}
                                  {% if member.profile.github %}
                                      <a href="https://github.com/{{ member.profile.github }}" class="card-link" target="_blank"><i class="fab fa-github"></i></a>
                                  {% endif %}
                                  {% if member.profile.website %}
                                      <a href="{{ member.profile.website }}" class="card-link" target="_blank"><i class="fas fa-globe"></i></a>
                                  {% endif %}
                                  {% if member.profile.google_scholar %}
                                      <a href="{{ member.profile.google_scholar }}" class="card-link" target="_blank"><i class="ai ai-google-scholar-square ai-lg"></i></a>
                                  {% endif %}
                              </div>
                              {% if member.profile.address %}
                                <p class="card-text">
                                    <small class="text-muted"><i class="fas fa-thumbtack"></i> {{ member.profile.address | replace: '<br />', ', ' }}</small>
                                </p>
                              {% endif %}
                          </div>
                      </div>
                  </div>
              </div>
          </p>
      </div>
      <br />
      {% endfor %}
  </div>
  <br />
  {% endfor %}

{% else %}
  <p>No members available.</p>
{% endif %}
