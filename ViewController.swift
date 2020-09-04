//
//  ViewController.swift
//  PhotoLoco
//
//  Created by Abhijaat Gupta on 8/19/20.
//  Copyright © 2020 myTime. All rights reserved.
//

import UIKit
import CoreLocation
import MapKit

class ViewController: UIViewController, CLLocationManagerDelegate {
    
    
    @IBOutlet weak var mapView: MKMapView!
    
    private var locationManager:CLLocationManager?
    var lat: Double!
    var long: Double!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        locationManager = CLLocationManager()
        locationManager?.requestAlwaysAuthorization()
        locationManager?.startUpdatingLocation()
        locationManager?.delegate = self
        
    }
    //called everytime location updates with most recent location at end of locations array
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let loc = locations.last {
            lat = loc.coordinate.latitude
            long = loc.coordinate.longitude
            updateMapLocation(location: loc)
        }
    }
    
    func updateMapLocation(location: CLLocation){
        let point = MKPointAnnotation();
        point.title = "You are here"
        point.coordinate = location.coordinate
        self.mapView.removeAnnotations(self.mapView.annotations)
        self.mapView.addAnnotation(point)
        let viewRegion = MKCoordinateRegion(center: location.coordinate, latitudinalMeters: 2000, longitudinalMeters: 2000)
        self.mapView.setRegion(viewRegion, animated: true)
    }

}

