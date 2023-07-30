from branca.element import MacroElement
from jinja2 import Template

from folium.elements import JSCSSMixin
from folium.utilities import parse_options


class Geocoder(JSCSSMixin, MacroElement):
    """A simple geocoder for Leaflet that by default uses OSM/Nominatim.

    Please respect the Nominatim usage policy:
    https://operations.osmfoundation.org/policies/nominatim/

    Parameters
    ----------
    collapsed: bool, default False
        If True, collapses the search box unless hovered/clicked.
    position: str, default 'topright'
        Choose from 'topleft', 'topright', 'bottomleft' or 'bottomright'.
    add_marker: bool, default True
        If True, adds a marker on the found location.

    For all options see https://github.com/perliedman/leaflet-control-geocoder

    """

    _template = Template(
        """
        {% macro script(this, kwargs) %}
            class CustomGeocoder extends L.Control.Geocoder.Nominatim {
                constructor() {
                    super();
                    this.suggestions = [];
                }
                setSuggestions(arr){
                  this.suggestions = arr;
                }
                createSuggestionFromMarker(marker){
                   //have changed here to lowercase:
                  this.suggestions.push({name: (marker.options.title).toLowerCase(), marker: marker});
                }
                getResultsOfSuggestions(query){
                  var results = [];
                  this.suggestions.forEach((point)=>{
                    if(point.name.toLowerCase().indexOf(query.toLowerCase()) > -1){
                        if(point.marker){
                        point.center = point.marker.getLatLng();
                      }
                      point.center = L.latLng(point.center);
                      point.bbox = point.center.toBounds(100);
                      results.push(point);
                    }
                  });
                  return results;
                }
                geocode(query, resultFnc, context) {
                  var that = this;
                  var callback = function(results){
                    var sugg = that.getResultsOfSuggestions(query);
                    resultFnc.call(this,sugg.concat(results));
                  }
                  L.Control.Geocoder.Nominatim.prototype.geocode.call(that,query, callback, context);
                }
              }
              
            var geocoder = new CustomGeocoder();
            var nastavenia = {{ this.options|tojson }};
            nastavenia.geocoder = geocoder;
            var control = L.Control.geocoder(nastavenia).on('markgeocode', function(e) {
                {{ this._parent.get_name() }}.setView(e.geocode.center, 11);
            }).addTo({{ this._parent.get_name() }});
            
            var suggestions = {{ this.suggestions|safe }};
            geocoder.setSuggestions(suggestions);

        {% endmacro %}
    """
    )

    default_js = [
        (
            "Control.Geocoder.js",
            "https://unpkg.com/leaflet-control-geocoder/dist/Control.Geocoder.js",
        )
    ]
    default_css = [
        (
            "Control.Geocoder.css",
            "https://unpkg.com/leaflet-control-geocoder/dist/Control.Geocoder.css",
        )
    ]

    def __init__(self, collapsed=False, position="topright", add_marker=True, suggestions=None, **kwargs):
        super().__init__()
        if suggestions is None:
            suggestions = []
        self._name = "Geocoder"
        self.options = parse_options(
            collapsed=collapsed,
            position=position,
            defaultMarkGeocode=add_marker,
            **kwargs
        )
        self.suggestions = suggestions
